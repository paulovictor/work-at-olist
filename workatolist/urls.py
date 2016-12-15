from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework import routers

from marketplaces.views import ChannelViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/docs/')),
    url(r'^api/', include(router.urls), name='api'),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
