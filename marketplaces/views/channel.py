from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from marketplaces.models import Channel
from marketplaces.serializers import CategorySerializer
from marketplaces.serializers import ChannelSerializer
from marketplaces.serializers.channel import ChannelListSerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChannelSerializer
    list_serializer_class = ChannelListSerializer
    queryset = Channel.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ChannelListSerializer
        if self.action == 'retrieve':
            return ChannelSerializer

    @detail_route(methods=['get'], url_path='category/(?P<category_slug>[^/.]+)')
    def category(self, request, slug=None, category_slug=None):
        category = self.get_object().categories.filter(slug=category_slug).first()
        return Response(CategorySerializer(category).data)
