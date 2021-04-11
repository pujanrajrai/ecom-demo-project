from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_name',
            'price',
            'photo',
            'category',
            'sub_category',
            'brand_name',
            'description',
            'stock'
        ]
