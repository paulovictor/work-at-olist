from pprint import pprint

from django.db import models

# Create your models here.
from django.utils.text import slugify


class NameSlugMixin(models.Model):
    name = models.CharField('Category Name', max_length=255)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.strip())
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(NameSlugMixin):
    parent = models.ForeignKey('self', null=True)
    channel = models.ForeignKey('marketplaces.Channel', related_name='categories')

    def __str__(self):
        return self.slug

    @classmethod
    def create_categories(cls, _channel, lines):
        new_categories = []
        for line in lines[1:len(lines) - 1]:
            categories = line.split('/')
            _parent = None
            for category in categories:
                _category, created = cls.objects.get_or_create(
                    name=category,
                    parent=_parent,
                    channel=_channel
                )
                _parent = _category
                if _category not in new_categories:
                    new_categories.append(_category)
            pprint(line)
        return new_categories

    @staticmethod
    def delete_old_categories(new_categories, old_categories):
        to_delete = [category for category in old_categories if category not in new_categories]
        for _category in to_delete:
            pprint('Category {0} deleted'.format(_category.name))
            _category.delete()



class Channel(NameSlugMixin):
    pass
