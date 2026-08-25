from pathlib import Path

import yaml
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.catalogue.models import Category, Product, ProductImage, ProductVariant

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

CATEGORY_FIELDS = {f.name for f in Category._meta.fields} - {'id', 'slug'}
PRODUCT_FIELDS = {f.name for f in Product._meta.fields} - {'id', 'slug', 'category', 'created_at', 'updated_at'}
VARIANT_FIELDS = {f.name for f in ProductVariant._meta.fields} - {'id', 'product', 'sku'}


class Command(BaseCommand):
    help = (
        'Create/update categories, products, variants and images from the catalogue '
        'YAML file (default: catalogue_data/catalogue.yaml). Re-run after editing the '
        'file or adding photos to backend/media/products/<category-slug>/<product-slug>/.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            default=str(Path(settings.BASE_DIR) / 'catalogue_data' / 'catalogue.yaml'),
            help='Path to the catalogue YAML file.',
        )
        parser.add_argument(
            '--prune',
            action='store_true',
            help='Permanently delete products that are no longer listed in the file '
                 '(default: just hide them by marking inactive).',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Print what would change without writing to the database.',
        )

    def handle(self, *args, **options):
        path = Path(options['file'])
        if not path.exists():
            raise CommandError(f'Catalogue file not found: {path}')

        data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        dry_run = options['dry_run']
        prune = options['prune']

        seen_category_slugs = set()
        seen_product_slugs = set()

        for cat_item in data.get('categories', []):
            slug = cat_item['slug']
            seen_category_slugs.add(slug)
            category = self._sync_category(slug, cat_item, dry_run)

            for prod_item in cat_item.get('products', []):
                seen_product_slugs.add(prod_item['slug'])
                self._sync_product(category, prod_item, dry_run)

        removed_products = Product.objects.exclude(slug__in=seen_product_slugs)
        if prune:
            count = removed_products.count()
            if not dry_run:
                removed_products.delete()
            self.stdout.write(f'Removed {count} product(s) no longer listed in the file.')
        else:
            count = removed_products.filter(is_active=True).count()
            if not dry_run:
                removed_products.update(is_active=False)
            self.stdout.write(f'Hid {count} product(s) no longer listed in the file (marked inactive).')

        removed_categories = Category.objects.exclude(slug__in=seen_category_slugs).filter(is_active=True)
        hidden_cat_count = removed_categories.count()
        if not dry_run:
            removed_categories.update(is_active=False)
        self.stdout.write(f'Hid {hidden_cat_count} categor{"y" if hidden_cat_count == 1 else "ies"} no longer listed in the file.')

        if dry_run:
            self.stdout.write(self.style.WARNING('Dry run — no changes were saved.'))
        else:
            self.stdout.write(self.style.SUCCESS('Catalogue synced.'))

    def _sync_category(self, slug, item, dry_run):
        category, created = Category.objects.get_or_create(slug=slug, defaults={'name': item.get('name', slug)})
        for field in CATEGORY_FIELDS:
            if field in item:
                setattr(category, field, item[field])
        category.is_active = item.get('is_active', True)
        if not dry_run:
            category.save()
        self.stdout.write(f'{"Created" if created else "Updated"} category: {slug}')
        return category

    def _sync_product(self, category, item, dry_run):
        slug = item['slug']
        product, created = Product.objects.get_or_create(
            slug=slug,
            defaults={'category': category, 'name': item.get('name', slug), 'description': item.get('description', '')},
        )
        product.category = category
        for field in PRODUCT_FIELDS:
            if field in item:
                setattr(product, field, item[field])
        product.is_active = item.get('is_active', True)
        if not dry_run:
            product.save()
        self.stdout.write(f'  {"Created" if created else "Updated"} product: {slug}')

        if not dry_run:
            self._sync_variants(product, item.get('variants', []))
            self._sync_images(product, category, item)

    def _sync_variants(self, product, variants_data):
        seen_skus = set()
        for variant_item in variants_data:
            sku = variant_item['sku']
            seen_skus.add(sku)
            fields = {k: v for k, v in variant_item.items() if k in VARIANT_FIELDS}
            ProductVariant.objects.update_or_create(product=product, sku=sku, defaults=fields)
        removed = product.variants.exclude(sku__in=seen_skus)
        removed_count = removed.count()
        removed.delete()
        if variants_data or removed_count:
            self.stdout.write(f'    Synced {len(variants_data)} variant(s), removed {removed_count}.')

    def _sync_images(self, product, category, item):
        folder_name = item.get('photos_folder', f'{category.slug}/{product.slug}')
        folder = Path(settings.MEDIA_ROOT) / 'products' / folder_name
        explicit = item.get('photos')

        if explicit:
            entries = [(photo['file'], photo.get('alt_text', '')) for photo in explicit]
        elif folder.exists():
            entries = [
                (path.name, '')
                for path in sorted(folder.iterdir())
                if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
            ]
        else:
            entries = []

        product.images.all().delete()
        for order, (filename, alt_text) in enumerate(entries, start=1):
            ProductImage.objects.create(
                product=product,
                image=f'products/{folder_name}/{filename}',
                alt_text=alt_text or product.name,
                display_order=order,
            )

        if entries:
            self.stdout.write(f'    Linked {len(entries)} photo(s) from media/products/{folder_name}/')
        else:
            self.stdout.write(self.style.WARNING(f'    No photos found in media/products/{folder_name}/'))
