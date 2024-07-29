from django.urls import path
from .views.store import *
urlpatterns = [
        path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),

]