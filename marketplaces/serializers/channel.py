from rest_framework import serializers

from marketplaces.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('get_tree')

    class Meta:
        model = Channel
        fields = ('name', 'slug', 'categories')

    @staticmethod
    def get_tree(obj):
        return obj.tree


class ChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'slug')
