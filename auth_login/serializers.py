from rest_framework import serializers

from provider_details.models import Store
from .models import *


###### customer serializers
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username','name', 'phone']


class CustomerCreateAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id','name','username','email','phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password field is write-only
        }


class CustomerPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['latitude','longitude','address']

#### end customer


###### provider serializers
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id','username','name', 'phone']


class   ProviderCreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id','name','category','username','phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password field is write-only
        }
           
  

class ProviderPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)


class ProviderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['latitude','longitude','address']

#### end customer
class ProviderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name','email',]