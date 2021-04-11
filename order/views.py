from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, HttpResponse
from products.models import Products
from shop_profile.models import ShopProfile
from .forms import OrderForm
from .models import Order
from ecommerce.decorators import is_seller
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Order


@login_required
def addtocart(request, slug):
    user = request.user
    products = Products.objects.get(slug=slug)
    form_data = {"products": products.id, 'user': user}
    form = OrderForm(form_data)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return HttpResponse("error")


@login_required
def view_cart(request):
    cart_item = Order.objects.filter(user=request.user).filter(is_bought=False)
    print(cart_item)
    total = 0
    for cart in cart_item:
        total = total + int(cart.products.price)
    print(total)
    context = {'cart_item': cart_item, 'total': total}
    return render(request, 'order/cart.html', context)


@login_required()
def remove_from_cart(request, card_id):
    if request.method == "POST":
        Order.objects.filter(id=card_id).delete()
        return redirect('order:view_cart')
    return redirect('/')


@login_required()
def checkout(request):
    if request.method == "POST":
        Order.objects.filter(user=request.user).update(is_bought=True)
        return redirect('landing_page:landing_page')


@login_required()
def order_details(request):
    order = Order.objects.filter(user=request.user)
    context = {"order": order}
    return render(request, 'order/order_details.html', context)


@login_required()
@is_seller()
# @is_order_owner()
def shop_order_details(request, username):
    if not ShopProfile.objects.filter(owner=request.user).filter(shop_user_name=username).exists():
        raise PermissionDenied
    order = Order.objects.filter(products__shop_product__shop_user_name=username)
    context = {"order": order, "username": username}
    return render(request, 'order/shop_order_details.html', context)


@login_required()
@is_seller()
def is_send(request, id, username):
    if request.method == 'POST':
        Order.objects.filter(id=id).update(is_send=True)
        return HttpResponseRedirect(f'/order/shop_order_details/{username}')


@login_required()
@is_seller()
def is_delivered(request, id, username):
    if request.method == 'POST':
        Order.objects.filter(id=id).update(is_delivered=True)
        return HttpResponseRedirect(f'/order/shop_order_details/{username}')
