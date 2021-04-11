from django import forms
from django.core.exceptions import ValidationError

from .models import SellerProfile


class SellerProfileFrom(forms.ModelForm):
    first_name = forms.CharField(min_length=3, max_length=50)
    last_name = forms.CharField(min_length=3, max_length=50)
    mobile_number = forms.IntegerField(max_value=9999999999, min_value=9800000000)
    citizenship_number = forms.IntegerField(min_value=10000, max_value=1000000000000000000)
    citizenship_front = forms.ImageField()

    class Meta:
        model = SellerProfile
        fields = [
            'first_name',
            'last_name',
            'mobile_number',
            'citizenship_number',
            'citizenship_front',
            'citizenship_back',
            'temp_add',
            'per_add'
        ]
