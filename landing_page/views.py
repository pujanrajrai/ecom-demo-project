from django.shortcuts import render, HttpResponse
from products.models import Products

# Create your views here.
from shop_profile.models import ShopProfile


def landing_page(request):
    products = Products.objects.all().order_by('-created_date')
    context = {"products": products}
    return render(request, 'landing_page/landing_page.html', context)


def shop_landing_page(request, username):
    if not ShopProfile.objects.filter(shop_user_name=username).exists():
        return HttpResponse('Shop Profile Doesnot Exist')
    products = Products.objects.filter(shop_product__shop_user_name=username)
    context = {"products": products, "username": username}
    return render(request, 'landing_page/shop_landing_page.html', context)


def search(request):
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search')
    context = {}
    if search_type == 'shop':
        search_result = ShopProfile.objects.filter(shop_user_name=search_key).order_by('-id')[:10]
        context['search_result'] = search_result
    elif search_type == 'product':
        search_result = Products.objects.filter(product_name=search_key).order_by('-id')[:10]
        context['search_result'] = search_result
    print(context)
    return render(request, 'landing_page/search.html', context)


def test(request):
    return render(request,'dashboard/home.html')
