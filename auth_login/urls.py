from django.urls import path
from .views import *
from .subscription_views import *
urlpatterns = [
    ##  for customer links
    path('customer-info-profile',CustomerDataAPIView.as_view(),name='customer-data-get-request'),
    path('customer-create-account',CustomerCreateAccountAPIView.as_view(),name='customer-data-post-request'),
    path('customer-login', CustomerAuthToken.as_view()),
    path('customer-set-address', CustomerAddressRetrieveUpdateDestroyAPIView.as_view(), name='customer-addresses-list-create'),
    path('customer-password-update', CustomerPasswordUpdateAPIView.as_view(), name='customer-password-update'),

    
    
    ### end customer



    ## for provider links
    path('provider-info-profile',ProviderDataAPIView.as_view(),name='customer-data-get-request'),
    path('provider-create-account',ProviderCreateAccountAPIView.as_view(),name='customer-data-post-request'),
    path('provider-login', ProviderAuthToken.as_view()),
    path('provider-set-address', ProviderAddressRetrieveUpdateDestroyAPIView.as_view(), name='customer-addresses-list-create'),
    path('provider-info-update', ProviderInfoRetrieveUpdateAPIView.as_view(), name='provider-info-update-retrive'),

    ### end provider
    
    ###subscription details //admin panal
    path('subscription/<int:id>',subscription,name="subscription details"),
    path('subscription_details/<int:id>',subscription_details,name="subscription details")
]