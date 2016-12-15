import os
from unittest import TestCase

from django.core.management import call_command
from django.utils.six import StringIO

from marketplaces.format_exception import FormatError
from marketplaces.models import Category, Channel


class ImportCategoriesCommandTestCase(TestCase):
    def setUp(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    def test_import_csv_file(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures/categories.csv'))
        call_command('importcategories', 'walmart', file),

        self.assertTrue(Channel.objects.exists())
        self.assertEqual(Category.objects.all().count(), 23)

    def test_format_error_when_import_doc_file(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures/categories.doc'))
        with self.assertRaises(FormatError):
            call_command('importcategories', 'walmart', file)
