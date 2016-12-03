from pprint import pprint

from django.db import models

# Create your models here.
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class NameSlugMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.strip())
        super().save(*args, **kwargs)


class Category(MPTTModel, NameSlugMixin):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    channel = models.ForeignKey('marketplaces.Channel', related_name='categories')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.slug

    @classmethod
    def create_categories(cls, _channel, lines):
        new_categories = []
        for line in lines[1:len(lines) - 1]:
            categories = line.split('/')
            _parent = None
            for category in categories:
                _category_name = category.strip()
                _category, created = cls.objects.get_or_create(
                    name=_category_name,
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

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
