import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.catalogue.models import Category, Product, ProductVariant


@pytest.mark.django_db
def test_product_api_returns_catalogue():
    category = Category.objects.create(
        name='Curtains',
        slug='curtains',
        description='Soft and airy window textiles for living spaces.',
    )
    product = Product.objects.create(
        category=category,
        name='Ivory Linen Curtains',
        slug='ivory-linen-curtains',
        short_name='Ajrakh Block Print Door Curtain',
        sku='CUR-COT-AJR-IVO-7X48-S2',
        hsn_code='6303',
        sub_category='Door Curtain — Eyelet / Ring Top',
        collection_name='Gujarat ki Khushboo — Kutch Ajrakh Series',
        gujarat_heritage=True,
        gujarat_heritage_note='Ajrakh block print from Kutch, Gujarat.',
        primary_material='100% Kora Cotton',
        fabric_blend='Pure 100% cotton — no synthetic blend',
        fabric_gsm='190 GSM',
        fabric_texture='Plain weave, matte finish, soft natural hand-feel with slight texture',
        lining='Unlined — single layer, light filtering',
        transparency='Light Filter — 40-50% light reduction',
        handloom_or_machine='Handloom woven — pit loom, Bhavnagar district artisan',
        dye_type='Natural dyes: Indigo, Madder, Pomegranate rind',
        eco_tags='Handloom Mark India ✓ | Azo-free natural dyes ✓',
        width_per_panel='48 inches (122 cm)',
        length_drop='7 feet (213 cm)',
        pack_contents='Set of 2 panels',
        sizes_available='5 ft | 7 ft | 9 ft',
        custom_size_available=True,
        custom_size_note='WhatsApp us with measurements for custom sizing.',
        heading_tape_width='4 inch standard header tape',
        bottom_hem='3 inch double-fold hem',
        fullness_ratio_guide='For door: order 2 panels of 48" width for good gather',
        primary_colour='Ivory / Off-White',
        accent_colours='Indigo Blue, Rust Red, Earthy Gold',
        colour_family='Earthy Neutrals',
        print_pattern='Block Print — Ajrakh geometric medallion',
        print_technique='Hand Block Printed using carved wooden blocks',
        pattern_scale='Medium',
        pattern_repeat='22 cm vertical repeat',
        surface_finish='Matte',
        other_colour_options='Sage Green, Navy Blue, Terracotta',
        hanging_style='Eyelet / Ring Top',
        eyelet_size='4 cm inner diameter',
        rod_compatibility='Round rods up to 1.5" dia',
        best_suited_for='Living Room, Bedroom, Puja Room, Main Door',
        installation='Slide eyelets onto rod and mount brackets',
        hardware_included=False,
        tie_back_tassel='2 matching kora cotton tie-backs included',
        washing='Machine wash cold 30°C',
        detergent='Mild liquid detergent only',
        drying='Shade dry — do NOT tumble dry',
        ironing='Medium heat on reverse side',
        first_wash='Wash separately in cold water before first use',
        colour_fastness='Grade 4/5',
        dry_cleaning='Dry cleaning safe but unnecessary',
        storage='Store rolled in breathable cotton bag away from sunlight',
        mrp='1599.00',
        website_selling_price='1299.00',
        amazon_price='1399.00',
        flipkart_price='1349.00',
        gst_rate='5% GST',
        cost_price='520.00',
        festival_sale_price='999.00',
        pack_variants_and_prices='1 Panel: ₹699 | 2 Panel Set: ₹1,299 | 4 Panel Bundle: ₹2,399',
        shipping_weight='850g per set',
        current_stock=36,
        reorder_level=8,
        lead_time='Ready stock: dispatch in 24 hours',
        packaging='Rolled in recycled tissue and kraft paper sleeve',
        packed_dimensions='48cm L × 14cm W × 14cm H',
        country_of_origin='India — Made in Bhavnagar, Gujarat',
        brand_manufacturer='Home Decor Brand, Bhavnagar, Gujarat',
        return_policy='7-day return for manufacturing defects only',
        short_description_social='Hand block-printed in the centuries-old Ajrakh tradition of Kutch.',
        amazon_bullets='Handloom woven • Natural dye • Light filtering • Easy care',
        primary_seo_keywords='handloom curtains india | ajrakh block print curtains',
        amazon_backend_keywords='block print curtain set 7ft | natural dye cotton curtain',
        description='A light, breathable curtain set designed for airy bedrooms and lounges.',
        material='Cotton linen blend',
        care_instructions='Gentle machine wash below 30°C.',
        is_featured=True,
    )
    ProductVariant.objects.create(
        product=product,
        sku='IVORY-LINEN-01',
        size='5x7 ft',
        colour='Ivory',
        price='2499.00',
        compare_at_price='3299.00',
        stock_quantity=12,
    )

    client = APIClient()
    response = client.get(reverse('product-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    product_result = response.data['results'][0]
    assert product_result['name'] == 'Ivory Linen Curtains'
    assert product_result['sku'] == 'CUR-COT-AJR-IVO-7X48-S2'
    assert product_result['primary_material'] == '100% Kora Cotton'
    assert product_result['print_pattern'] == 'Block Print — Ajrakh geometric medallion'
    assert product_result['variants'][0]['price'] == '2499.00'


@pytest.mark.django_db
def test_seed_command_creates_sample_catalogue():
    from django.core.management import call_command

    call_command('seed_catalogue', '--clear')

    assert Category.objects.filter(slug='curtains').exists()
    assert Product.objects.filter(slug='ivory-linen-curtains').exists()
    assert ProductVariant.objects.filter(sku='IVORY-LINEN-01').exists()
