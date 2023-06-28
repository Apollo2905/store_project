from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField()
    is_discounted = models.BooleanField()
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('store.Brand', on_delete=models.CASCADE)
    image = models.ImageField(default='default-product-image.png', blank=True)

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f'Image #{self.pk}'


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    guest = models.ForeignKey('store.Guest', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Guest(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'guests'
