from django.db import models
from accounts.models import MyUser


# Create your models here.

class ShopProfile(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    shop_registered_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_user_name = models.CharField(max_length=10, unique=True)
    shop_owner_name = models.CharField(max_length=150)
    shop_address = models.CharField(max_length=100)
    shop_warehouse_address = models.CharField(max_length=100)
    shop_returned_address = models.CharField(max_length=100)
    shop_category = models.CharField(max_length=100)
    shop_detail_description = models.CharField(max_length=1000)
    shop_pan_card = models.ImageField()
    shop_phone_number = models.BigIntegerField()
    shop_owner_phone_number = models.BigIntegerField()
    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_user_name






