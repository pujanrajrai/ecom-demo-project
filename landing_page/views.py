from django.shortcuts import render,HttpResponse
from products.models import Products


# Create your views here.

def landing_page(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'landing_page/home.html',context)


def test(request):
    print(request.user.is_admin)
    return HttpResponse('hello')
