from rest_framework import serializers
from .models import *
from auth_login.serializers import CustomerSerializer
from provider_details.models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name','image']
        
class ProductSerializer(serializers.ModelSerializer):
    price_after_offer = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','name','image','price','offers','price_after_offer']
        
    def get_price_after_offer(self, obj):
            if obj.offers is not None:
                return obj.price_after_offer
            return obj.price
        
class ServiceOrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    customer=CustomerSerializer()
    class Meta:
        model = ServiceOrder
        fields =['id','customer','service',]
        read_only_fields = ['customer','accept']
        
class ProductOrderSerializer(serializers.ModelSerializer):
    product= ProductSerializer(read_only=True)
    customer=CustomerSerializer()    
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
    store_name=serializers.CharField(source='product.store.name', read_only=True)
    total_price = serializers.SerializerMethodField()
    coupon=serializers.CharField(source='coupon.name', read_only=True)
    customer=CustomerSerializer()
    class Meta:
        model = ProductOrder
        fields = ['id','product','customer','store_name','quantity','total_price','coupon','price_with_coupon','status']
        read_only_fields = ['customer',]
        
    def get_total_price(self, obj):
        if obj.product.offers:
            return obj.quantity * obj.product.price_after_offer
        else:
            return obj.quantity * obj.product.price
        

class ServiceBookOrderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer()
    specialist=serializers.CharField(source='specialist.name', read_only=True)
    service_name=serializers.CharField(source='service.name', read_only=True)
    price=serializers.CharField(source='service.price', read_only=True)
    price_after_offer=serializers.CharField(source='service.price_after_offer', read_only=True)
    offer=serializers.CharField(source='service.offers', read_only=True)
    coupon=serializers.CharField(source='coupon.name', read_only=True)
    main_service=serializers.CharField(source='service.main_service', read_only=True)
    category=serializers.CharField(source='service.main_service.category', read_only=True)
    store_name = serializers.SerializerMethodField()
    store_image = serializers.SerializerMethodField()
   
    def get_store_name(self, obj):
        return obj.service.store.name if obj.service.store else None

    def get_store_image(self, obj):
        return obj.service.store.image.url if obj.service.store and obj.service.store.image else None

    class Meta:
        model = ServiceOrder
        fields = ('customer', 'main_service','service_name','price','offer','price_after_offer','coupon','price_with_coupon','service', 'category','specialist', 'time_start', 'date', 'duration', 'status', 'store_name', 'store_image')

###############PROVIDER##################################
class ServiceOrderProviderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer(read_only=True)
    service_name=serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = ServiceOrder
        fields = ['id','time_start', 'date','service_name','customer']
        read_only_fields = ['customer',]


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
        fields = ['specialist','service','date','duration','status']
        read_only_fields = ['customer','date','duration']

class ProductOrderProviderAcceptSerializer(serializers.ModelSerializer):
    product= ProductSerializer(read_only=True)
    customer=CustomerSerializer(read_only=True)
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
        
