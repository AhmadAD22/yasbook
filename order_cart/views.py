from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ProductOrder, ServiceOrder
from .serializers import *

class ProductOrderCreateView(generics.CreateAPIView):
    serializer_class = ProductOrderBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def perform_create(self, serializer):
        customer=Customer.objects.get(username=self.request.user.username)

        serializer.save(customer=customer)


class ProductOrderListView(generics.ListAPIView):
    serializer_class = ProductOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer=Customer.objects.get(username=self.request.user.username)
        
        return ProductOrder.objects.filter(customer=customer)
    

class ServiceOrderCreateView(generics.CreateAPIView):
    serializer_class = ServiceBookOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        customer=Customer.objects.get(username=self.request.user.username)

        serializer.save(customer=customer)

class ServiceOrderListView(generics.ListAPIView):
    serializer_class = ServiceOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        customer=Customer.objects.get(username=self.request.user.username)
        return ServiceOrder.objects.filter(customer=customer)
    


### provider

class ServiceOrderProviderListView(generics.ListAPIView):
    serializer_class = ServiceOrderProviderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        provider = Provider.objects.get(username=self.request.user.username)
        # store = Store.objects.get(provider=provider)
        # service =Service.objects.get(store=store)
        return ServiceOrder.objects.filter(service__store__provider=provider)

class ProductOrderProviderListView(generics.ListAPIView):
    serializer_class = ProductOrderProviderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        provider = Provider.objects.get(username=self.request.user.username)
        return ProductOrder.objects.filter(product__store__provider=provider)
    


class ProductOrderProviderAcceptView(generics.UpdateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderProviderAcceptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        product_order_id = self.kwargs.get('pk')
        return ProductOrder.objects.get(pk=product_order_id)

class ServiceOrderProviderAcceptView(generics.UpdateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderProviderAcceptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        service_order_id = self.kwargs.get('pk')
        return ServiceOrder.objects.get(pk=service_order_id)
