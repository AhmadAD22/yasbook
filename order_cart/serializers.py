from rest_framework import serializers
from .models import *
from auth_login.serializers import CustomerSerializer
from collections import defaultdict

from provider_details.models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name','image']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','image']
        
class ServiceOrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    customer=serializers.CharField(source='customer.name', read_only=True)
    class Meta:
        model = ServiceOrder
        fields =['id','customer','service',]
        read_only_fields = ['customer','accept']
        
class ProductOrderSerializer(serializers.ModelSerializer):
    product= ProductSerializer(read_only=True)
    customer=serializers.CharField(source='customer.name', read_only=True)
    class Meta:
        model = ProductOrder
        fields =['id','customer','product','quantity',]
        read_only_fields = ['customer','accept']




class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['image', 'name', 'about']


class ProductOrderBookSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model = ProductOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']
        

class ServiceBookOrderSerializer(serializers.ModelSerializer):
    specialist=serializers.CharField(source='specialist.name', read_only=True)
    service_name=serializers.CharField(source='service.name', read_only=True)
    main_service=serializers.CharField(source='service.main_service', read_only=True)
    category=serializers.CharField(source='service.main_service.category', read_only=True)

    class Meta:
        model = ServiceOrder
        fields = '__all__'
        read_only_fields = ['customer','accept']



###############PROVIDER##################################
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
    specialist=serializers.CharField(source='specialist.name', read_only=True)
    service = ServiceSerializer(read_only=True)
    class Meta:
        model = ServiceOrder
        fields = ['accept','specialist','service','date','duration']
        read_only_fields = ['customer','date','duration']


class ProductOrderProviderAcceptSerializer(serializers.ModelSerializer):
    product= ProductSerializer(read_only=True)
    customer=serializers.CharField(source='customer.name', read_only=True)
    # specialist=serializers.CharField(source='specialist.name', read_only=True)
    class Meta:
        model = ProductOrder
        fields = ['accept','customer','product','quantity']
  
        
class ServiceAndProductOrderProviderSerializer(serializers.Serializer):
    product = ProductOrderSerializer(many=True)
    service = ServiceOrderSerializer(many=True)
##############END PROVIDER########
    
###########CART###########################    
#to add and update
class ServiceCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCartItem
        fields = ('id',  'service', 'specialist', 'date', 'duration')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')
        
#just to display in the cart
class ServiceCartItemDesplaySerializer(serializers.ModelSerializer):
    service_id = serializers.PrimaryKeyRelatedField(source='service', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    service_image = serializers.ImageField(source='service.image', read_only=True)
    service_price = serializers.DecimalField(source='service.price', read_only=True, max_digits=10, decimal_places=2)


    class Meta:
        model = ServiceCartItem
        fields = ('id', 'service_id', 'service_name','service_price' ,'specialist', 'date', 'duration', 'service_image')

#just to display in the cart
class CartItemDesplaySerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_image = serializers.ImageField(source='product.image', read_only=True)
    product_price = serializers.DecimalField(source='product.price', read_only=True, max_digits=10, decimal_places=2)
    class Meta:
        model = CartItem
        fields = ('id', 'product_id', 'product_name', 'product_price', 'quantity', 'product_image')

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemDesplaySerializer(many=True, source='cartitem_set')
    service_cart_items = ServiceCartItemDesplaySerializer(many=True, source='servicecartitem_set')

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'cart_items', 'service_cart_items','total_price']
        read_only_fields = ('id',)
        
#########END CART###############################################

#############StoreSpecialistBook##############
class StoreSpecialistBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSpecialist
        fields = ['id', 'name','image']
        
