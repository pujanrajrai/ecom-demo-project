from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SellerProfileFrom
from .models import SellerProfile
from ecommerce.decorators import is_seller


# Create your views here.
@login_required()
@is_seller()
def seller_profile_create(request):
    if SellerProfile.objects.filter(owner=request.user).exists():
        return redirect('seller_profile:seller_profile_view')
    if request.method == 'POST':
        forms = SellerProfileFrom(request.POST, request.FILES)
        if forms.is_valid():
            seller_profile = SellerProfile(
                owner=request.user,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                mobile_number=request.POST['mobile_number'],
                citizenship_number=request.POST['citizenship_number'],
                temp_add=request.POST['temp_add'],
                per_add=request.POST['per_add'],
                citizenship_front=request.FILES['citizenship_front'],
                citizenship_back=request.FILES['citizenship_back'],
            )
            seller_profile.save()
            return redirect('shop_profile:shop_profile_show')
        else:
            context = {'errors': forms.errors}
            return render(request, 'seller_profile/seller_profile_create.html', context)

    return render(request, 'seller_profile/seller_profile_create.html')


@login_required()
@is_seller()
def seller_profile_view(request):
    if not SellerProfile.objects.filter(owner=request.user).exists():
        return redirect('seller_profile:seller_profile_create')
    profile = SellerProfile.objects.filter(owner=request.user)
    context = {"profile": profile}
    return render(request, 'seller_profile/seller_profile_show.html', context)
