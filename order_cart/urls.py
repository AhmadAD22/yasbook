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


]