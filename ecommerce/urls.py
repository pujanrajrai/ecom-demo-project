from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('order/', include('order.urls')),
                  path('', include('landing_page.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('seller/profile/', include('seller_profile.urls')),
                  path('seller/shop/profile/', include('shop_profile.urls')),
                  path('product/', include('products.urls')),
                  # path('messages/', include('messages.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
