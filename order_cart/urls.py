from django.urls import path
from .views import *

urlpatterns = [
    path('customer-book-product/', ProductOrderCreateView.as_view(), name='product-order-create'),
    path('customer-get-book-product/', ProductOrderListView.as_view(), name='product-order-create'),
    path('customer-book-service/', ServiceOrderCreateView.as_view(), name='service-order-create'),
    path('customer-get-book-service/', ServiceOrderListView.as_view(), name='service-order-create'),

    ## provider

    path('provider-get-book-service/', ServiceOrderProviderListView.as_view(), name='service-order-create'),
    path('provider-put-accept-service/<int:pk>/', ServiceOrderProviderAcceptView.as_view(), name='service-order-provider-accept'),

    path('provider-get-book-product/', ProductOrderProviderListView.as_view(), name='product-order-create'),
    path('provider-put-accept-product/<int:pk>/', ProductOrderProviderAcceptView.as_view(), name='service-order-provider-accept'),
    path('service-product-order-List/', ServiceAndProductListView.as_view(), name='product-order-create'),
    ######Cart
    path('cart/item/', CartItemAPIView.as_view(), name='cart-item-api'),
    path('cart/item/<int:item_id>/', CartItemAPIView.as_view(), name='cart-item-delete-api'),
    path('cart/service/', ServiceCartItemAPIView.as_view(), name='service-cart-item-api'),
    path('cart/service/<int:item_id>/', ServiceCartItemAPIView.as_view(), name='service-cart-item-delete-api'),
    path('cart/checkout/', CartCheckoutAPIView.as_view(), name='cart-checkout'),
    path('cart/', CartAPIView.as_view(), name='cart'),
 ########Specialist-availability
    path('specialist-availability/<int:service_id>', SpecialistAvailabilityView.as_view(), name='specialist-availability'),
 


]