from django.db import models
# Create your models here.

from products.models import Products
from accounts.models import MyUser


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now=True)
    is_bought = models.BooleanField(default=False)
    is_send = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.products.product_name

    def price(self):
        return self.products.price



    # def product_order_shop(self):
    #     return self.products.shop_product
