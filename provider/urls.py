from django.urls import path
from.views.login import *
from .views.main import *
from .views.products import *
from .views.service import *
from .views.coupon import *
from .views.specialist import *

urlpatterns = [
    path('login',login_view,name="provider-login"),
    path('',provider_main_dashboard,name="provider-main-dashboard"),
    # Products
    path('product/create/', create_product, name='provider-create_product'),
    path('product/list/',product_list, name='provider-product_list'),
    path('product/update/<int:id>/', update_product, name='provider-update_product'),
    path('product/delete/<int:id>/', delete_product, name='provider-delete_product'),
    #Services
    path('services/', service_list, name='provider-service_list'),
    path('services/create/', create_service, name='provider-create_service'),
    path('services/update/<int:id>/',update_service, name='provider-update_service'),
    path('services/delete/<int:id>/',delete_service, name='provider-delete_service'),
    #Coupon
    path('coupons/', coupon_list, name='provider-coupon_list'),
    path('coupons/create/', create_coupon, name='provider-create_coupon'),
    path('coupons/update/<int:id>/',update_coupon, name='provider-update_coupon'),
    path('coupons/delete/<int:id>/',delete_coupon, name='provider-delete_coupon'),
    
    path('specialists/', store_specialist_list, name='store-specialist-list'),
    path('specialists/create/',store_specialist_create, name='store-specialist-create'),
    path('specialists/<int:pk>/update/', store_specialist_update, name='store-specialist-update'),
    path('specialists/<int:pk>/delete/',store_specialist_delete, name='store-specialist-delete'),
             ]   