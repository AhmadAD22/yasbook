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

class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields = ['id','name']
        read_only_fields = ['name']
        
class StoreSpecialistSerializer(serializers.ModelSerializer):
    specialistworks = serializers.PrimaryKeyRelatedField(many=True, queryset=MainService.objects.all())
    class Meta:
        model = StoreSpecialist
        fields = ['id', 'name', 'phone','image', 'specialistworks']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['specialistworks'] = MainServiceSerializer(instance.specialistworks.all(), many=True).data
        return representation
    # def destroy(self, request, *args, **kwargs):
        # instance = self.get_object()

        # # Add your custom delete logic here
        # # For example, you can perform additional checks or actions before deleting the instance

        # self.perform_destroy(instance)
        
    
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

class ReviewsStorSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer()
    class Meta:
        model = Reviews
        exclude = ['store']
        
class StoreAdminServicesSerializer(serializers.ModelSerializer):
    main_service=serializers.CharField(source='main_service.name', read_only=True)
    class Meta:
        model = StoreAdminServices
        fields = ["main_service"]
    
class NearbyFeaturedStoreOrderSerializer(serializers.ModelSerializer):
    address=serializers.CharField(source='provider.address', read_only=True)
    reviews = serializers.SerializerMethodField()
    main_services=serializers.SerializerMethodField()
    class Meta:
        model = Store
        fields = ['id','image', 'name', 'about','address','reviews','main_services']
        
    def get_reviews(self, obj):
        reviews_data = ReviewsStorSerializer(obj.reviews_set.all(), many=True).data
        ratings = [review['rating'] for review in reviews_data]
        average = sum(ratings) / len(ratings) if ratings else 0
        return {"count":len(reviews_data),'average':average}
    def get_main_services(self, obj):
        main_services=StoreAdminServices.objects.filter(store=obj)
        
        return [ main_service.main_service.name  for main_service in main_services ]
    

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
        reviews_data = ReviewsSerializer(obj.reviews_set.all(), many=True).data
        ratings = [review['rating'] for review in reviews_data]
        average = sum(ratings) / len(ratings) if ratings else 0
        return {'reviews_data':reviews_data,"count":len(reviews_data),'average':average}

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