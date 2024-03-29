
from django.contrib import admin
from django.urls import path,include
from auth_login.views import redirect_to_admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('admin_material.urls')),
    path('admin/', admin.site.urls),
    path("", redirect_to_admin, name="to_admin"),


    path('user/',include('auth_login.urls')),

    path('category/',include('categroy.urls')),

    path('store/',include('provider_details.urls')),

    path('order/',include('order_cart.urls')),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)