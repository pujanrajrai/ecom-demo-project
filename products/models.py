from django.db import models
from accounts.models import MyUser
from shop_profile.models import ShopProfile
from django.utils.text import slugify


# Create your models here.

class Products(models.Model):
    shop_product = models.ForeignKey(ShopProfile, on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    stock = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name + "-" + str(self.id))
        super(Products, self).save(*args, **kwargs)
