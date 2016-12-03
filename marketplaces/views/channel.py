from rest_framework import viewsets

from marketplaces.models import Channel
from marketplaces.serializers import ChannelSerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
    lookup_field = 'slug'
