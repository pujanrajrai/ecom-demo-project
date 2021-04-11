from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ShopProfileForm
from .models import ShopProfile
from ecommerce.decorators import is_seller


# Create your views here.
@login_required
@is_seller()
def shop_profile_create(request):
    if request.method == 'POST':
        forms = ShopProfileForm(request.POST, request.FILES)
        if forms.is_valid():
            shop_profile = ShopProfile(
                owner=request.user,
                shop_registered_name=request.POST.get('shop_registered_name'),
                shop_name=request.POST.get('shop_name'),
                shop_user_name=request.POST.get('shop_user_name'),
                shop_owner_name=request.POST.get('shop_owner_name'),
                shop_address=request.POST.get('shop_address'),
                shop_warehouse_address=request.POST.get('shop_warehouse_address'),
                shop_returned_address=request.POST.get('shop_returned_address'),
                shop_category=request.POST.get('shop_category'),
                shop_detail_description=request.POST.get('shop_detail_description'),
                shop_pan_card=request.FILES.get('shop_pan_card'),
                shop_phone_number=request.POST.get('shop_phone_number'),
                shop_owner_phone_number=request.POST.get('shop_owner_phone_number'),
            )
            shop_profile.save()
            return redirect('shop_profile:shop_profile_show')
        else:
            context = {"error": forms.errors}
            return render(request, 'shop_profile/shop_profile_create.html', context)
    return render(request, 'shop_profile/shop_profile_create.html')


@login_required
@is_seller()
def show_shop_profile(request):
    my_shop_profile = ShopProfile.objects.filter(owner=request.user)
    context = {"shop_profile": my_shop_profile}
    return render(request, 'shop_profile/shop_profile_show.html', context)
