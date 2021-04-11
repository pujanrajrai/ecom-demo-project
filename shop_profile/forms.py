from django import forms
from .models import ShopProfile


class ShopProfileForm(forms.ModelForm):
    shop_registered_name = forms.CharField(max_length=100, min_length=2)
    shop_name = forms.CharField(max_length=100, min_length=2)
    shop_owner_name = forms.CharField(max_length=100, min_length=2)
    shop_address = forms.CharField(max_length=100, min_length=2)
    shop_warehouse_address = forms.CharField(max_length=100, min_length=2)
    shop_returned_address = forms.CharField(max_length=100, min_length=2)
    shop_category = forms.CharField(max_length=100, min_length=2)
    shop_detail_description = forms.CharField(max_length=1000, min_length=2)
    shop_pan_card = forms.ImageField()
    shop_phone_number = forms.IntegerField(min_value=9800000000, max_value=9999999999)

    class Meta:
        model = ShopProfile
        fields = [
            'shop_registered_name',
            'shop_name',
            'shop_user_name',
            'shop_owner_name',
            'shop_address',
            'shop_warehouse_address',
            'shop_returned_address',
            'shop_category',
            'shop_detail_description',
            'shop_pan_card',
            'shop_phone_number',
            'shop_owner_phone_number'
        ]
