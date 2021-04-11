from django.db import models
from accounts.models import MyUser


# Create your models here.

class SellerProfile(models.Model):
    owner = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.PositiveIntegerField()
    citizenship_number = models.PositiveIntegerField()
    citizenship_front = models.ImageField()
    citizenship_back = models.ImageField()
    temp_add = models.CharField(max_length=50)
    per_add = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
