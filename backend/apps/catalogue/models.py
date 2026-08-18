from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        ordering = ['-is_featured', 'name']

    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    short_name = models.CharField(max_length=180, blank=True)
    sku = models.CharField(max_length=120, blank=True)
    hsn_code = models.CharField(max_length=20, blank=True)
    sub_category = models.CharField(max_length=180, blank=True)
    collection_name = models.CharField(max_length=220, blank=True)
    gujarat_heritage = models.BooleanField(default=False)
    gujarat_heritage_note = models.TextField(blank=True)
    primary_material = models.CharField(max_length=200, blank=True)
    fabric_blend = models.CharField(max_length=200, blank=True)
    fabric_gsm = models.CharField(max_length=80, blank=True)
    fabric_texture = models.TextField(blank=True)
    lining = models.CharField(max_length=200, blank=True)
    transparency = models.CharField(max_length=200, blank=True)
    handloom_or_machine = models.CharField(max_length=200, blank=True)
    dye_type = models.CharField(max_length=200, blank=True)
    eco_tags = models.TextField(blank=True)
    width_per_panel = models.CharField(max_length=80, blank=True)
    length_drop = models.CharField(max_length=80, blank=True)
    pack_contents = models.CharField(max_length=200, blank=True)
    sizes_available = models.CharField(max_length=200, blank=True)
    custom_size_available = models.BooleanField(default=False)
    custom_size_note = models.TextField(blank=True)
    heading_tape_width = models.CharField(max_length=80, blank=True)
    bottom_hem = models.CharField(max_length=80, blank=True)
    fullness_ratio_guide = models.TextField(blank=True)
    primary_colour = models.CharField(max_length=120, blank=True)
    accent_colours = models.CharField(max_length=200, blank=True)
    colour_family = models.CharField(max_length=80, blank=True)
    print_pattern = models.CharField(max_length=200, blank=True)
    print_technique = models.CharField(max_length=200, blank=True)
    pattern_scale = models.CharField(max_length=80, blank=True)
    pattern_repeat = models.CharField(max_length=80, blank=True)
    surface_finish = models.CharField(max_length=80, blank=True)
    other_colour_options = models.CharField(max_length=200, blank=True)
    hanging_style = models.CharField(max_length=120, blank=True)
    eyelet_size = models.CharField(max_length=80, blank=True)
    rod_compatibility = models.CharField(max_length=200, blank=True)
    best_suited_for = models.CharField(max_length=200, blank=True)
    installation = models.TextField(blank=True)
    hardware_included = models.BooleanField(default=False)
    tie_back_tassel = models.CharField(max_length=200, blank=True)
    washing = models.CharField(max_length=200, blank=True)
    detergent = models.CharField(max_length=200, blank=True)
    drying = models.CharField(max_length=200, blank=True)
    ironing = models.CharField(max_length=200, blank=True)
    first_wash = models.TextField(blank=True)
    colour_fastness = models.CharField(max_length=80, blank=True)
    dry_cleaning = models.CharField(max_length=200, blank=True)
    storage = models.TextField(blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    website_selling_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amazon_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flipkart_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gst_rate = models.CharField(max_length=80, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    festival_sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pack_variants_and_prices = models.CharField(max_length=240, blank=True)
    shipping_weight = models.CharField(max_length=80, blank=True)
    current_stock = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)
    lead_time = models.CharField(max_length=200, blank=True)
    packaging = models.TextField(blank=True)
    packed_dimensions = models.CharField(max_length=120, blank=True)
    country_of_origin = models.CharField(max_length=200, blank=True)
    brand_manufacturer = models.CharField(max_length=200, blank=True)
    return_policy = models.TextField(blank=True)
    short_description_social = models.TextField(blank=True)
    amazon_bullets = models.TextField(blank=True)
    primary_seo_keywords = models.TextField(blank=True)
    amazon_backend_keywords = models.TextField(blank=True)
    description = models.TextField()
    material = models.CharField(max_length=120, blank=True)
    care_instructions = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=64, unique=True)
    size = models.CharField(max_length=80, blank=True)
    colour = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name} — {self.sku}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/')
    alt_text = models.CharField(max_length=180, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'id']
