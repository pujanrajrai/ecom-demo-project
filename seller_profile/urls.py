from django.urls import path
from . import views

app_name = 'seller_profile'

urlpatterns = [
    path('create/', views.seller_profile_create, name='seller_profile_create'),
    path('view/', views.seller_profile_view, name='seller_profile_view')
]
