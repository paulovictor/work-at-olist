from pprint import pprint

from django.db import models
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from mptt.templatetags.mptt_tags import cache_tree_children


class NameSlugMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        abstract = True


class Category(MPTTModel, NameSlugMixin):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    channel = models.ForeignKey('marketplaces.Channel', related_name='categories')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.strip())
        if self.parent:
            self.slug = '{0}-{1}'.format(self.parent.slug, self.slug)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.slug

    @property
    def parents(self):
        return self.get_ancestors().values('name', 'slug')

    @property
    def subcategories(self):
        return self.get_children().values('name', 'slug')

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

    @classmethod
    def recursive_categories(cls, category):
        result = {
            'slug': category.slug,
            'name': category.name,
        }
        children = [cls.recursive_categories(child) for child in category.get_children()]
        if children:
            result['sub-category'] = children
        return result


class Channel(NameSlugMixin):

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.strip())
        super().save(*args, **kwargs)

    @property
    def tree(self):
        _categories = self.categories.all()
        dict_child = cache_tree_children(_categories)
        tree = []
        for child in dict_child:
            tree.append(Category.recursive_categories(child))
        return tree
