from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField()
    is_discounted = models.BooleanField()
    # slug = AutoSlugField(populate_from='title', editable=True, always_update=True)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def save(self, **kwargs):
        save.slug = slugify(self.title)
        super(Product, self).save(**kwargs)
