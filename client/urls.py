from django.urls import path
from .views.store import *
from .views.service import *
urlpatterns = [
        #Store
        path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
        
        
        path('service-filter/', ServiceFilterAPIView.as_view(), name='service-filter'),
        path('service-search/', ServiceSearchAPIView.as_view(), name='service-search'),
        path('service/<int:category_id>/', ServicesByCategoryAPIView.as_view(), name='service-by-category'),
        path('service/<int:category_id>/<int:main_service_id>/', ServicesByCategoryAndMAinServiceAPIView.as_view(), name='service-by-category'),
        path('service-details/<int:service_id>/', ServiceDetailsAPIView.as_view(), name='service-by-category'),
        

]