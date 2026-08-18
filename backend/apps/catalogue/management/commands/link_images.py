from django.core.management.base import BaseCommand
from pathlib import Path
from apps.catalogue.models import Product, ProductImage


class Command(BaseCommand):
    help = 'Link product images from the media folder to products in the catalogue.'

    def handle(self, *args, **options):
        # Get the Ivory Linen Curtains product
        try:
            product = Product.objects.get(slug='ivory-linen-curtains')
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Product "Ivory Linen Curtains" not found. Run seed_catalogue first.'))
            return

        # Clear existing images for this product
        product.images.all().delete()

        # Image paths in media folder
        image_names = [
            'Curtains/images.jpeg',
            'Curtains/images (1).jpeg',
            'Curtains/images (2).jpeg',
            'Curtains/images (3).jpeg',
        ]

        # Create ProductImage records
        for idx, image_name in enumerate(image_names, 1):
            ProductImage.objects.create(
                product=product,
                image=image_name,
                alt_text=f'Ajrakh Block Print Curtain - View {idx}',
                display_order=idx,
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Added image: {image_name}'))

        self.stdout.write(self.style.SUCCESS(f'\n✓ Successfully linked {len(image_names)} images to "{product.name}"'))
