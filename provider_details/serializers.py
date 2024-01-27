from rest_framework import serializers
from .models import *
from auth_login.serializers import CustomerSerializer

## for provider app
class StoreStorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = StoreStory
        fields = ['image', ]
class StoreSerializer(serializers.ModelSerializer):
    story_of_store=StoreStorySerializer(read_only=True)
    class Meta:
        model = Store
        fields = ['image', 'name', 'about','story_of_store']

class StoreForProviderWhenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['provider']


class StoreSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSpecialist
        fields = ['id','name']

class StoreOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOpening
        fields = ['id','day', 'time_start', 'time_end']


class StoreGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreGallery
        exclude = ['store']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['store']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['store']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        exclude = ['customer']


#### store ui fpr customer

from rest_framework import serializers
from .models import Store, StoreSpecialist, StoreOpening, StoreGallery, Service, Product

class StoreASpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSpecialist
        exclude = ['store']

class StoreAOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOpening
        exclude = ['store']

class StoreAGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreGallery
        exclude = ['store']

class ServiceASerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['store']

class ProductASerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['store']

class ReviewsSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer()
    class Meta:
        model = Reviews
        exclude = ['store']

class StoreADetailSerializer(serializers.ModelSerializer):
    specialists = serializers.SerializerMethodField()
    openings = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()


    def get_specialists(self, obj):
        # Customize the serialization of 'specialists' field here
        return StoreASpecialistSerializer(obj.storespecialist_set.all(), many=True).data

    def get_openings(self, obj):
        # Customize the serialization of 'openings' field here
        return StoreAOpeningSerializer(obj.storeopening_set.all(), many=True).data

    def get_gallery(self, obj):
        # Customize the serialization of 'gallery' field here
        return StoreAGallerySerializer(obj.storegallery_set.all(), many=True).data

    def get_services(self, obj):
        # Customize the serialization of 'services' field here
        return ServiceASerializer(obj.service_set.all(), many=True).data

    def get_products(self, obj):
        # Customize the serialization of 'products' field here
        return ProductASerializer(obj.product_set.all(), many=True).data

    def get_reviews(self, obj):
        return ReviewsSerializer(obj.reviews_set.all(), many=True).data

    class Meta:
        model = Store
        fields = ['id','image','name','about','created_at','openings', 'gallery', 'products', 'services', 'specialists','reviews']

class StoreFollowingListSerializer(serializers.ModelSerializer):
    store=StoreSerializer(read_only=True)

    class Meta:
        model = FollowingStore
        fields = '__all__'
        read_only_fields=['customer']

class StoreFollowingSerializer(serializers.ModelSerializer):
    # store=StoreSellerSerializer(read_only=True)
    class Meta:
        model = FollowingStore
        fields = '__all__'
        read_only_fields=['customer']