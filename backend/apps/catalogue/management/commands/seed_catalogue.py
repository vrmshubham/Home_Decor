from django.core.management.base import BaseCommand

from apps.catalogue.models import Category, Product, ProductVariant


class Command(BaseCommand):
    help = 'Seed the catalogue with a small set of sample product data.'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing catalogue records before seeding.')

    def handle(self, *args, **options):
        if options['clear']:
            ProductVariant.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()

        curtains, _ = Category.objects.get_or_create(
            slug='curtains',
            defaults={
                'name': 'Curtains',
                'description': 'Light, textured and room-brightening window coverings.',
                'display_order': 1,
            },
        )

        bedsheets, _ = Category.objects.get_or_create(
            slug='bedsheets',
            defaults={
                'name': 'Bedsheets',
                'description': 'Soft cotton blends for everyday comfort.',
                'display_order': 2,
            },
        )

        rugs, _ = Category.objects.get_or_create(
            slug='rugs',
            defaults={
                'name': 'Rugs & Mats',
                'description': 'Layered textures that define a room.',
                'display_order': 3,
            },
        )

        catalog = [
            {
                'category': curtains,
                'name': 'Ivory Linen Curtains',
                'slug': 'ivory-linen-curtains',
                'short_name': 'Ajrakh Block Print Door Curtain',
                'sku': 'CUR-COT-AJR-IVO-7X48-S2',
                'hsn_code': '6303',
                'sub_category': 'Door Curtain — Eyelet / Ring Top',
                'collection_name': 'Gujarat ki Khushboo — Kutch Ajrakh Series',
                'gujarat_heritage': True,
                'gujarat_heritage_note': 'Ajrakh block print from Kutch, Gujarat.',
                'primary_material': '100% Kora Cotton',
                'fabric_blend': 'Pure 100% cotton — no synthetic blend',
                'fabric_gsm': '190 GSM',
                'fabric_texture': 'Plain weave, matte finish, soft natural hand-feel with slight texture',
                'lining': 'Unlined — single layer, light filtering',
                'transparency': 'Light Filter — 40-50% light reduction',
                'handloom_or_machine': 'Handloom woven — pit loom, Bhavnagar district artisan',
                'dye_type': 'Natural dyes: Indigo, Madder, Pomegranate rind',
                'eco_tags': 'Handloom Mark India ✓ | Azo-free natural dyes ✓',
                'width_per_panel': '48 inches (122 cm)',
                'length_drop': '7 feet (213 cm)',
                'pack_contents': 'Set of 2 panels',
                'sizes_available': '5 ft | 7 ft | 9 ft',
                'custom_size_available': True,
                'custom_size_note': 'WhatsApp us with measurements for custom sizing.',
                'heading_tape_width': '4 inch standard header tape',
                'bottom_hem': '3 inch double-fold hem',
                'fullness_ratio_guide': 'For door: order 2 panels of 48" width for good gather',
                'primary_colour': 'Ivory / Off-White',
                'accent_colours': 'Indigo Blue, Rust Red, Earthy Gold',
                'colour_family': 'Earthy Neutrals',
                'print_pattern': 'Block Print — Ajrakh geometric medallion',
                'print_technique': 'Hand Block Printed using carved wooden blocks',
                'pattern_scale': 'Medium',
                'pattern_repeat': '22 cm vertical repeat',
                'surface_finish': 'Matte',
                'other_colour_options': 'Sage Green, Navy Blue, Terracotta',
                'hanging_style': 'Eyelet / Ring Top',
                'eyelet_size': '4 cm inner diameter',
                'rod_compatibility': 'Round rods up to 1.5" dia',
                'best_suited_for': 'Living Room, Bedroom, Puja Room, Main Door',
                'installation': 'Slide eyelets onto rod and mount brackets',
                'hardware_included': False,
                'tie_back_tassel': '2 matching kora cotton tie-backs included',
                'washing': 'Machine wash cold 30°C',
                'detergent': 'Mild liquid detergent only',
                'drying': 'Shade dry — do NOT tumble dry',
                'ironing': 'Medium heat on reverse side',
                'first_wash': 'Wash separately in cold water before first use',
                'colour_fastness': 'Grade 4/5',
                'dry_cleaning': 'Dry cleaning safe but unnecessary',
                'storage': 'Store rolled in breathable cotton bag away from sunlight',
                'mrp': '1599.00',
                'website_selling_price': '1299.00',
                'amazon_price': '1399.00',
                'flipkart_price': '1349.00',
                'gst_rate': '5% GST',
                'cost_price': '520.00',
                'festival_sale_price': '999.00',
                'pack_variants_and_prices': '1 Panel: ₹699 | 2 Panel Set: ₹1,299 | 4 Panel Bundle: ₹2,399',
                'shipping_weight': '850g per set',
                'current_stock': 36,
                'reorder_level': 8,
                'lead_time': 'Ready stock: dispatch in 24 hours',
                'packaging': 'Rolled in recycled tissue and kraft paper sleeve',
                'packed_dimensions': '48cm L × 14cm W × 14cm H',
                'country_of_origin': 'India — Made in Bhavnagar, Gujarat',
                'brand_manufacturer': 'Home Decor Brand, Bhavnagar, Gujarat',
                'return_policy': '7-day return for manufacturing defects only',
                'short_description_social': 'Hand block-printed in the centuries-old Ajrakh tradition of Kutch.',
                'amazon_bullets': 'Handloom woven • Natural dye • Light filtering • Easy care',
                'primary_seo_keywords': 'handloom curtains india | ajrakh block print curtains',
                'amazon_backend_keywords': 'block print curtain set 7ft | natural dye cotton curtain',
                'description': 'Airy and elegant linen-blend curtains with a softly textured finish.',
                'material': 'Cotton linen blend',
                'care_instructions': 'Gentle machine wash below 30°C. Air dry in shade.',
                'is_featured': True,
                'variants': [
                    {
                        'sku': 'IVORY-LINEN-01',
                        'size': '5x7 ft',
                        'colour': 'Ivory',
                        'price': '2499.00',
                        'compare_at_price': '3299.00',
                        'stock_quantity': 12,
                    }
                ],
            },
            {
                'category': bedsheets,
                'name': 'Sandstone Stripe Bedsheet',
                'slug': 'sandstone-stripe-bedsheet',
                'description': 'A warm, earthy stripe set created for calm and comfortable bedroom styling.',
                'material': 'Premium cotton',
                'care_instructions': 'Wash separately in cold water. Do not bleach.',
                'is_featured': True,
                'variants': [
                    {
                        'sku': 'SANDSTONE-STRIPE-01',
                        'size': 'Queen',
                        'colour': 'Sandstone',
                        'price': '1899.00',
                        'compare_at_price': '2399.00',
                        'stock_quantity': 8,
                    }
                ],
            },
            {
                'category': rugs,
                'name': 'Terracotta Weave Rug',
                'slug': 'terracotta-weave-rug',
                'description': 'Hand-inspired woven texture in terracotta tones for cosy, layered floors.',
                'material': 'Polyester blend',
                'care_instructions': 'Vacuum gently. Spot clean with mild detergent.',
                'is_featured': False,
                'variants': [
                    {
                        'sku': 'TERRACOTTA-WEAVE-01',
                        'size': '4x6 ft',
                        'colour': 'Terracotta',
                        'price': '2999.00',
                        'compare_at_price': '3999.00',
                        'stock_quantity': 5,
                    }
                ],
            },
        ]

        for item in catalog:
            product, created = Product.objects.get_or_create(
                slug=item['slug'],
                defaults={
                    'category': item['category'],
                    'name': item['name'],
                    'short_name': item.get('short_name', ''),
                    'sku': item.get('sku', ''),
                    'hsn_code': item.get('hsn_code', ''),
                    'sub_category': item.get('sub_category', ''),
                    'collection_name': item.get('collection_name', ''),
                    'gujarat_heritage': item.get('gujarat_heritage', False),
                    'gujarat_heritage_note': item.get('gujarat_heritage_note', ''),
                    'primary_material': item.get('primary_material', ''),
                    'fabric_blend': item.get('fabric_blend', ''),
                    'fabric_gsm': item.get('fabric_gsm', ''),
                    'fabric_texture': item.get('fabric_texture', ''),
                    'lining': item.get('lining', ''),
                    'transparency': item.get('transparency', ''),
                    'handloom_or_machine': item.get('handloom_or_machine', ''),
                    'dye_type': item.get('dye_type', ''),
                    'eco_tags': item.get('eco_tags', ''),
                    'width_per_panel': item.get('width_per_panel', ''),
                    'length_drop': item.get('length_drop', ''),
                    'pack_contents': item.get('pack_contents', ''),
                    'sizes_available': item.get('sizes_available', ''),
                    'custom_size_available': item.get('custom_size_available', False),
                    'custom_size_note': item.get('custom_size_note', ''),
                    'heading_tape_width': item.get('heading_tape_width', ''),
                    'bottom_hem': item.get('bottom_hem', ''),
                    'fullness_ratio_guide': item.get('fullness_ratio_guide', ''),
                    'primary_colour': item.get('primary_colour', ''),
                    'accent_colours': item.get('accent_colours', ''),
                    'colour_family': item.get('colour_family', ''),
                    'print_pattern': item.get('print_pattern', ''),
                    'print_technique': item.get('print_technique', ''),
                    'pattern_scale': item.get('pattern_scale', ''),
                    'pattern_repeat': item.get('pattern_repeat', ''),
                    'surface_finish': item.get('surface_finish', ''),
                    'other_colour_options': item.get('other_colour_options', ''),
                    'hanging_style': item.get('hanging_style', ''),
                    'eyelet_size': item.get('eyelet_size', ''),
                    'rod_compatibility': item.get('rod_compatibility', ''),
                    'best_suited_for': item.get('best_suited_for', ''),
                    'installation': item.get('installation', ''),
                    'hardware_included': item.get('hardware_included', False),
                    'tie_back_tassel': item.get('tie_back_tassel', ''),
                    'washing': item.get('washing', ''),
                    'detergent': item.get('detergent', ''),
                    'drying': item.get('drying', ''),
                    'ironing': item.get('ironing', ''),
                    'first_wash': item.get('first_wash', ''),
                    'colour_fastness': item.get('colour_fastness', ''),
                    'dry_cleaning': item.get('dry_cleaning', ''),
                    'storage': item.get('storage', ''),
                    'mrp': item.get('mrp', None),
                    'website_selling_price': item.get('website_selling_price', None),
                    'amazon_price': item.get('amazon_price', None),
                    'flipkart_price': item.get('flipkart_price', None),
                    'gst_rate': item.get('gst_rate', ''),
                    'cost_price': item.get('cost_price', None),
                    'festival_sale_price': item.get('festival_sale_price', None),
                    'pack_variants_and_prices': item.get('pack_variants_and_prices', ''),
                    'shipping_weight': item.get('shipping_weight', ''),
                    'current_stock': item.get('current_stock', 0),
                    'reorder_level': item.get('reorder_level', 0),
                    'lead_time': item.get('lead_time', ''),
                    'packaging': item.get('packaging', ''),
                    'packed_dimensions': item.get('packed_dimensions', ''),
                    'country_of_origin': item.get('country_of_origin', ''),
                    'brand_manufacturer': item.get('brand_manufacturer', ''),
                    'return_policy': item.get('return_policy', ''),
                    'short_description_social': item.get('short_description_social', ''),
                    'amazon_bullets': item.get('amazon_bullets', ''),
                    'primary_seo_keywords': item.get('primary_seo_keywords', ''),
                    'amazon_backend_keywords': item.get('amazon_backend_keywords', ''),
                    'description': item['description'],
                    'material': item['material'],
                    'care_instructions': item['care_instructions'],
                    'is_featured': item['is_featured'],
                },
            )

            for variant in item['variants']:
                ProductVariant.objects.get_or_create(
                    sku=variant['sku'],
                    defaults={
                        'product': product,
                        'size': variant['size'],
                        'colour': variant['colour'],
                        'price': variant['price'],
                        'compare_at_price': variant['compare_at_price'],
                        'stock_quantity': variant['stock_quantity'],
                    },
                )

        self.stdout.write(self.style.SUCCESS('Catalogue seeded successfully.'))
