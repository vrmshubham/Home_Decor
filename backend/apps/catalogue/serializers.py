from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('sku', 'size', 'colour', 'price', 'compare_at_price', 'stock_quantity')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'alt_text')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'short_name', 'sku', 'hsn_code', 'category', 'sub_category',
            'collection_name', 'gujarat_heritage', 'gujarat_heritage_note', 'primary_material',
            'fabric_blend', 'fabric_gsm', 'fabric_texture', 'lining', 'transparency',
            'handloom_or_machine', 'dye_type', 'eco_tags', 'width_per_panel', 'length_drop',
            'pack_contents', 'sizes_available', 'custom_size_available', 'custom_size_note',
            'heading_tape_width', 'bottom_hem', 'fullness_ratio_guide', 'primary_colour',
            'accent_colours', 'colour_family', 'print_pattern', 'print_technique', 'pattern_scale',
            'pattern_repeat', 'surface_finish', 'other_colour_options', 'hanging_style',
            'eyelet_size', 'rod_compatibility', 'best_suited_for', 'installation',
            'hardware_included', 'tie_back_tassel', 'washing', 'detergent', 'drying',
            'ironing', 'first_wash', 'colour_fastness', 'dry_cleaning', 'storage', 'mrp',
            'website_selling_price', 'amazon_price', 'flipkart_price', 'gst_rate',
            'cost_price', 'festival_sale_price', 'pack_variants_and_prices', 'shipping_weight',
            'current_stock', 'reorder_level', 'lead_time', 'packaging', 'packed_dimensions',
            'country_of_origin', 'brand_manufacturer', 'return_policy', 'short_description_social',
            'amazon_bullets', 'primary_seo_keywords', 'amazon_backend_keywords', 'description',
            'material', 'care_instructions', 'is_featured', 'variants', 'images'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')
