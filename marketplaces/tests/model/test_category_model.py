from unittest import TestCase

from model_mommy import mommy

from marketplaces.models import Category


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make('Category', name='teste')

    def tearDown(self):
        Category.objects.all().delete()

    def test_count_categories(self):
        mommy.make('Category', _quantity=9)
        self.assertEqual(Category.objects.count(), 10)

    def test_check_slug(self):
        self.assertEqual(self.category.slug, 'teste')
