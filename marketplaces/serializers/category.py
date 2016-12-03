from rest_framework import serializers

from marketplaces.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug', 'parents', 'subcategories')
