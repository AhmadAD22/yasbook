from django.shortcuts import render,redirect,get_object_or_404
from auth_login.models import ProviderSubscription,Provider
from auth_login.models import *
from order_cart.models import *


def provider_main_dashboard(request):
    return render(request,'provider/provider_main.html')