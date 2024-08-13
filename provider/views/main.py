from django.shortcuts import render,redirect,get_object_or_404
from auth_login.models import ProviderSubscription,Provider
from auth_login.models import *
from order_cart.models import *
from provider_details.models import * 

from django.db.models import Count
from datetime import datetime, timedelta
from django.db.models.functions import Extract,ExtractMonth


def get_service_orders_by_month():
    # Assuming you have a ServiceOrder model
    orders = ServiceOrder.objects.annotate(month=Extract('date', 'month')).values('month').annotate(count=Count('id')).order_by('month')

    labels = []
    data = []
    for order in orders:
        labels.append(datetime(2023, order['month'], 1).strftime('%b'))
        data.append(order['count'])

    return labels, data

def get_product_orders_by_month():
    orders = ProductOrder.objects.annotate(month=ExtractMonth('date')).values('month').annotate(count=Count('id')).order_by('month')

    labels = []
    data = []
    for order in orders:
        labels.append(datetime(2023, order['month'], 1).strftime('%b'))
        data.append(order['count'])

    return labels, data



def provider_main_dashboard(request):
    service_count=Service.objects.filter(store__provider__id=request.user.id).count()
    product_count=Product.objects.filter(store__provider__id=request.user.id).count()
    specialist_count=StoreSpecialist.objects.filter(store__provider__id=request.user.id).count()
    product_order_count=ProductOrder.objects.filter(product__store__provider__id=request.user.id,status=Status.COMPLETED).count()
    service_order_count=ServiceOrder.objects.filter(service__store__provider__id=request.user.id,status=Status.COMPLETED).count()
    subscription=ProviderSubscription.objects.filter(provider__id=request.user.id)
    if subscription:
        subscription=subscription.first()
        subscription=subscription.remaining_duration()
    else:
        subscription=0
        
    service_labels, service_data = get_service_orders_by_month()
    product_labels, product_data = get_product_orders_by_month()
    
    context={
        'service_count':service_count,
        'product_count':product_count,
        'specialist_count':specialist_count,
        'product_order_count':product_order_count,
        'service_order_count':service_order_count,
        'subscription':subscription,
        'service_labels':service_labels,
        'service_data':service_data,
        'product_labels':product_labels,
        'product_data':product_data,
        
    }
    
    
    return render(request,'provider/provider_main.html',context=context)