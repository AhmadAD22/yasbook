from rest_framework import serializers
from .models import *
from auth_login.serializers import CustomerSerializer

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['image', 'name', 'about']

class ServiceSerializer(serializers.ModelSerializer):
    store=StoreSerializer(read_only=True)
    class Meta:
        model = Service
        exclude = ['id']

class ProductSerializer(serializers.ModelSerializer):
    store=StoreSerializer(read_only=True)
    class Meta:
        model = Product
        fields = 'id'
class ProductOrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model = ProductOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']


class ProductOrderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']

class ServiceOrderSerializer(serializers.ModelSerializer):
    service=ServiceSerializer(read_only=True)

    class Meta:
        model = ServiceOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']

class ServiceBookOrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = ServiceOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']



## provider
class ServiceOrderProviderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer(read_only=True)

    class Meta:
        model = ServiceOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']


class ProductOrderProviderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer(read_only=True)
    class Meta:
        model = ProductOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']


class ServiceOrderProviderAcceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceOrder
        fields = ['accept']


class ProductOrderProviderAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['accept']