from django.core.urlresolvers import reverse
from model_mommy import mommy
from rest_framework.test import APITestCase


class ChannelTest(APITestCase):
    def setUp(self):
        _ = mommy.make(
            'Channel',
            name='walmart'
        )
        self.url_list = reverse('channel-list')

    def test_check_channel_on_list(self):
        response = self.client.get(self.url_list)
        results = response.data.get('results')
        channel_dict = {'name': 'walmart', 'slug': 'walmart'}
        self.assertIn(channel_dict, results)
        self.assertEqual(len(results), 1)

    def test_paginated_channel_list(self):
        mommy.make('Channel', name='teste', _quantity=100)
        response = self.client.get(self.url_list)
        results = response.data.get('results')
        self.assertEqual(len(results), 50)
