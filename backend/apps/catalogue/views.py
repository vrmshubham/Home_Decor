from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filterset_fields = ('category__slug', 'is_featured', 'material')
    search_fields = ('name', 'description', 'material')

    def get_queryset(self):
        return Product.objects.filter(is_active=True).select_related('category').prefetch_related('variants', 'images')
