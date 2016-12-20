from django.utils.text import slugify
from mptt.templatetags.mptt_tags import cache_tree_children

from marketplaces.models import NameSlugMixin, Category


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
