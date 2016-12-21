from unittest import TestCase

from model_mommy import mommy

from marketplaces.models import Channel


class ChannelModelTestCase(TestCase):
    def setUp(self):
        self.channel = mommy.make('Channel', name='teste')

    def tearDown(self):
        Channel.objects.all().delete()

    def test_count_channels(self):
        mommy.make('Channel', _quantity=9)
        self.assertEqual(Channel.objects.count(), 10)

    def test_check_slug(self):
        self.assertEqual(self.channel.slug, 'teste')
