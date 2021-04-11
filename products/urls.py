from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('add_product/<str:username>/', views.product_create, name='add_product'),
    path('show_product/<str:username>/', views.show_product, name='show_product'),

]
