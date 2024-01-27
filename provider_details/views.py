from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from auth_login.models import *
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


### for provider app
class StoreUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        provider=Provider.objects.get(username=self.request.user.username)
        return Store.objects.get(provider=provider)
    
class StoreSpecialistListCreateView(generics.ListCreateAPIView):
    serializer_class = StoreSpecialistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        provider=Provider.objects.get(username=self.request.user.username)

        return StoreSpecialist.objects.filter(store__provider=provider)

    def perform_create(self, serializer):
        provider=Provider.objects.get(username=self.request.user.username)
        store=Store.objects.get(provider=provider)
        serializer.save(store=store)

class StoreSpecialistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreSpecialist.objects.all()
    serializer_class = StoreSpecialistSerializer
    permission_classes = [IsAuthenticated]

class StoreOpeningListCreateView(generics.ListCreateAPIView):
    serializer_class = StoreOpeningSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        provider=Provider.objects.get(username=self.request.user.username)

        return StoreOpening.objects.filter(store__provider=provider)

    def perform_create(self, serializer):
        provider=Provider.objects.get(username=self.request.user.username)
        store=Store.objects.get(provider=provider)
        serializer.save(store=store)

class StoreOpeningRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreOpening.objects.all()
    serializer_class = StoreOpeningSerializer
    permission_classes = [IsAuthenticated]



class StoreGalleryListCreateView(generics.ListCreateAPIView):
    serializer_class = StoreGallerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        provider = Provider.objects.get(username=self.request.user.username)
        return StoreGallery.objects.filter(store__provider=provider)

    def perform_create(self, serializer):
        provider = Provider.objects.get(username=self.request.user.username)
        store = Store.objects.get(provider=provider)
        serializer.save(store=store)

class StoreGalleryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreGallery.objects.all()
    serializer_class = StoreGallerySerializer
    permission_classes = [IsAuthenticated]



class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        provider = Provider.objects.get(username=self.request.user.username)
        return Service.objects.filter(store__provider=provider)

    def perform_create(self, serializer):
        provider = Provider.objects.get(username=self.request.user.username)
        store = Store.objects.get(provider=provider)
        serializer.save(store=store)

class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        provider = Provider.objects.get(username=self.request.user.username)
        return Product.objects.filter(store__provider=provider)

    def perform_create(self, serializer):
        provider = Provider.objects.get(username=self.request.user.username)
        store = Store.objects.get(provider=provider)
        serializer.save(store=store)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]




class ReviewsListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Assuming you want reviews related to the authenticated user's store
        customer=Customer.objects.get(username=self.request.user.username)
        return Reviews.objects.filter(customer=customer)

    def perform_create(self, serializer):
        # Assuming you want to associate the review with the authenticated user's store
        customer=Customer.objects.get(username=self.request.user.username)
        serializer.save(customer=customer)

class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]


### for store ui



class StoreDetailView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreADetailSerializer
    permission_classes = []
    authentication_classes=[]


# from rest_framework import generics
# from .models import Service
# from .serializers import ServiceSerializer

class ServiceListByStoreAndMainServiceView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = []
    authentication_classes=[]
    def get_queryset(self):
        store_id = self.kwargs['store_id']
        main_service_id = self.kwargs['main_service_id']
        return Service.objects.filter(store_id=store_id, main_service=main_service_id)


class StoreListByMainServiceView(generics.ListAPIView):
    serializer_class = StoreADetailSerializer
    permission_classes = []
    authentication_classes=[]
    def get_queryset(self):
        main_service_id = self.kwargs['main_service_id']
        store_ids = StoreAdminServices.objects.filter(main_service=main_service_id).values_list('store_id', flat=True)
        return Store.objects.filter(id__in=store_ids)

class FollowingStoreListView(generics.ListAPIView):
    serializer_class = StoreFollowingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer=Customer.objects.get(username=self.request.user.username)
        return FollowingStore.objects.filter(customer=customer)
               
class FollowingStoreCreateView(generics.CreateAPIView):
    serializer_class = StoreFollowingSerializer
    permission_classes = [IsAuthenticated]


    
    def perform_create(self, serializer):
        customer=Customer.objects.get(username=self.request.user.username)
        store = serializer.validated_data['store']
        try:
            FollowingStore.objects.create(customer=customer, store=store)
        except IntegrityError:
            raise serializers.ValidationError("You are already following this store.")


class FollowingStoreDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer=Customer.objects.get(username=self.request.user.username)

        return FollowingStore.objects.filter(customer=customer)

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, store_id=self.kwargs['store_id'])

class FeaturedStoreFollowersOrderView(generics.ListAPIView):

    serializer_class = StoreADetailSerializer

    def get_queryset(self):
        main_service_id = self.kwargs['main_service_id']
        store_ids = StoreAdminServices.objects.filter(main_service=main_service_id).values_list('store_id', flat=True)
        return  Store.objects.filter(id__in=store_ids).annotate(num_followers=models.Count('followingstore')).order_by('-num_followers')