
from django.urls import path
from .views import NotificationAPIView,index

urlpatterns = [
    path('api/notifications/', NotificationAPIView.as_view(), name='home'),
    path('', index, name='index')

    # Other URL patterns
]