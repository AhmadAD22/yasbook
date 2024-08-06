from django.urls import path
from.views.login import *

urlpatterns = [
    path('login',login_view,name="provider-login")
]