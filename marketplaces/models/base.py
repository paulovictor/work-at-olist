from django.db import models


class NameSlugMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        abstract = True
