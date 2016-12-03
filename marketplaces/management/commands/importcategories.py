from django.core.management.base import BaseCommand

from marketplaces.models import Category, Channel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('channel', type=str)
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        file_name = options.get('file_name', None)
        channel = options.get('channel', None)
        _channel, _ = Channel.objects.get_or_create(name=channel)
        old_categories = _channel.categories.all()
        try:
            with open(file_name) as file:
                lines = file.read().splitlines()
                new_categories = Category.create_categories(_channel, lines)
                Category.delete_old_categories(new_categories, old_categories)
        except FileNotFoundError as error:
            raise error

        self.stdout.write(
            '{0} : Total of Categories = {1}'.format(
                _channel.name.title(),
                _channel.categories.count())
        )
