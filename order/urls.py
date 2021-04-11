from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('addtocart/<slug:slug>', views.addtocart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('order_details/', views.order_details, name='order_details'),
    path('shop_order_details/<str:username>', views.shop_order_details, name='shop_order_details'),
    path('checkout', views.checkout, name='checkout'),
    path('remove_from_cart/<int:card_id>', views.remove_from_cart, name='remove_from_cart'),
    path('is_send/<int:id>/<str:username>', views.is_send, name='is_send'),
    path('is_delivered/<int:id>/<str:username>', views.is_delivered, name='is_delivered'),
]
