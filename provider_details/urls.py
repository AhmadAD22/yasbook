from django.urls import path
from .views import *

urlpatterns = [
   ## for provider app
    path('update-store/', StoreUpdateView.as_view(), name='update-store'),
    path('store-specialists/', StoreSpecialistListCreateView.as_view(), name='store-specialist-list-create'),
    path('store-specialists/<int:pk>/', StoreSpecialistRetrieveUpdateDestroyView.as_view(), name='store-specialist-retrieve-update-destroy'),
    path('store-openings/', StoreOpeningListCreateView.as_view(), name='store-opening-list-create'),
    path('store-openings/<int:pk>/', StoreOpeningRetrieveUpdateDestroyView.as_view(), name='store-opening-retrieve-update-destroy'),

    ## adding deleteing updating galaery
    path('store-gallery/', StoreGalleryListCreateView.as_view(), name='store-gallery-list-create'),
    path('store-gallery/<int:pk>/', StoreGalleryRetrieveUpdateDestroyView.as_view(), name='store-gallery-retrieve-update-destroy'),


    ## adding deleteing updating store service
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroyView.as_view(), name='service-retrieve-update-destroy'),


    ## adding deleteing updating store products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),


    path('customer-reviews/', ReviewsListCreateView.as_view(), name='reviews-list-create'),
    path('api/reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyView.as_view(), name='reviews-retrieve-update-destroy'),

    path('customer-post-follow-store/', FollowingStoreCreateView.as_view(), name='follow-store-create'),
    path('customer-get-follow-store/', FollowingStoreListView.as_view(), name='follow-store-create'),
    path('unfollow-store/<int:store_id>/', FollowingStoreDeleteView.as_view(), name='follow-store-delete'),

    path('features-stores/<int:main_service_id>/', FeaturedStoreFollowersOrderView.as_view(), name='store-followers-order'),
    path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('store-services/<int:store_id>/<int:main_service_id>/', ServiceListByStoreAndMainServiceView.as_view(), name='service-list-by-store-and-main-service'),
    path('get-store-in-main-service/<int:main_service_id>/', StoreListByMainServiceView.as_view(), name='store-list-by-main-service'),
    # Add other URL patterns as needed
   
]