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
    channel = models.ForeignKey('marketplaces.Channel')

    def __str__(self):
        return self.slug

class Channel(NameSlugMixin):
    pass
