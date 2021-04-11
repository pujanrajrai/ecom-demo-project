from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductsForm
from .models import Products
from shop_profile.models import ShopProfile
from ecommerce.decorators import is_seller
from django.core.exceptions import PermissionDenied


# Create your views here.
@login_required
@is_seller()
def product_create(request, username):
    if not ShopProfile.objects.filter(owner=request.user).filter(shop_user_name=username).exists():
        raise PermissionDenied
    if request.method == 'POST':
        if not ShopProfile.objects.filter(owner=request.user).filter(shop_user_name=username).exists():
            raise PermissionDenied

        forms = ProductsForm(request.POST, request.FILES)
        if forms.is_valid():
            product = Products(
                shop_product=ShopProfile.objects.get(shop_user_name=username),
                owner=request.user,
                product_name=request.POST.get('product_name'),
                price=request.POST.get('price'),
                photo=request.FILES.get('photo'),
                category=request.POST.get('category'),
                sub_category=request.POST.get('sub_category'),
                brand_name=request.POST.get('brand_name'),
                description=request.POST.get('description'),
                stock=request.POST.get('stock')
            )
            product.save()
        else:
            print(forms.errors)
    return render(request, 'product/home.html', {"username": username})


@login_required()
@is_seller()
def show_product(request, username):
    if not ShopProfile.objects.filter(owner=request.user).filter(shop_user_name=username).exists():
        raise PermissionDenied
    product = Products.objects.filter(shop_product__shop_user_name=username)
    context = {"products": product, "username": username}
    return render(request, 'product/show_product.html', context)
