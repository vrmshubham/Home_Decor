from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVariant

class VariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'is_active', 'updated_at')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description', 'variants__sku')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (VariantInline, ImageInline)
