from django.core.urlresolvers import reverse
from model_mommy import mommy
from rest_framework.test import APITestCase


class ChannelBaseTest(APITestCase):
    def setUp(self):
        self.channel = mommy.make(
            'Channel',
            name='walmart'
        )


class ChannelListAPITest(ChannelBaseTest):
    def setUp(self):
        super().setUp()
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

    def test_invalid_post_method(self):
        data = {
            'name': 'Walmart'
        }
        response = self.client.post(self.url_list, data)
        error_msg = response.data.get('detail')
        self.assertEqual(405, response.status_code)
        self.assertEqual('Method "POST" not allowed.', error_msg)


class ChannelDetailAPITest(ChannelBaseTest):
    def setUp(self):
        super().setUp()
        self.url_detail = reverse('channel-detail', kwargs={'slug': self.channel.slug})

    def test_check_fields(self):
        response = self.client.get(self.url_detail)
        data = response.data
        channel = self.channel
        self.assertIn('slug', data)
        self.assertIn('name', data)
        self.assertIn('categories', data)
        self.assertEqual(channel.slug, data.get('slug'))
        self.assertEqual(channel.name, data.get('name'))
