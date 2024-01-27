from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='main-category-list-create'),
   
    path('main-service/<int:category_id>/',MainServiceListView.as_view(),name='facility-get-request'),


]