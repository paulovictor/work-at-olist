from rest_framework import viewsets

from marketplaces.models import Category
from marketplaces.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().select_related('parent')
    lookup_field = 'slug'
