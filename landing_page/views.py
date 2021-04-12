from django.shortcuts import render, HttpResponse
from products.models import Products

# Create your views here.
from shop_profile.models import ShopProfile


def landing_page(request):
    products = Products.objects.all().order_by('-created_date')
    context = {"products": products}
    return render(request, 'landing_page/home.html', context)


def shop_landing_page(request, username):
    if not ShopProfile.objects.filter(shop_user_name=username).exists():
        return HttpResponse('Shop Profile Doesnot Exist')
    products = Products.objects.filter(shop_product__shop_user_name=username)
    context = {"products": products, "username": username}
    return render(request, 'landing_page/shop_landing_page.html', context)


def test(request):
    print(request.user.is_admin)
    return HttpResponse('hello')
