from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import MyUser


# Create your views here.

def customer_register(request):
    if request.user.is_authenticated:
        return redirect('landing_page:landing_page')
    if request.method == 'POST':
        data = request.POST.copy()
        forms = RegisterForm(data)
        if forms.is_valid():
            user = MyUser(
                email=data['email'],
                password=make_password(data['password']),
                username=data['username'],
                date_of_birth=data['date_of_birth'],
                is_customer=True
            )
            user.save()
            user = auth.authenticate(email=data['email'], password=data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('landing_page:landing_page')
            return render(request, 'accounts/customer_register.html')
        else:
            print(forms.errors)
            context = {
                "error": forms.errors,
                "email": data['email'],
                "username": data['username'],
                "date_of_birth": data['date_of_birth']
            }
            return render(request, 'accounts/customer_register.html', context)

    return render(request, 'accounts/customer_register.html')


def seller_register(request):
    if request.user.is_authenticated:
        return redirect('landing_page:landing_page')
    if request.method == 'POST':
        data = request.POST.copy()
        forms = RegisterForm(data)
        print(data['username'])
        if forms.is_valid():
            print("form is valid")
            user = MyUser(
                email=data['email'],
                password=make_password(data['password']),
                username=data['username'],
                date_of_birth=data['date_of_birth'],
                is_seller=True,
            )
            user.save()
            user = auth.authenticate(email=data['email'], password=data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('seller_profile:seller_profile_create')
            return render(request, 'accounts/seller_registration.html')
        else:
            context = {"errors": forms.errors}
            return render(request, 'accounts/seller_registration.html', context)

    return render(request, 'accounts/seller_registration.html')


def login(request):
    form = {}
    if request.user.is_authenticated:
        return redirect('landing_page:landing_page')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('landing_page:landing_page')
            else:
                errors = "User name or password is incorrect"
                return render(request, 'accounts/login.html', {"errors": errors})
        return render(request, 'accounts/login.html', {"form": form})


def logout(request):
    auth.logout(request)
    return redirect('landing_page:landing_page')
