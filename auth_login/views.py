from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password,make_password

from provider_details.serializers import StoreForProviderWhenCreateSerializer

# Create your views here.
def redirect_to_admin(request):
    return HttpResponseRedirect(reverse("admin:login"))


#########  for customer views

class CustomerDataAPIView(generics.ListAPIView):
    serializer_class =CustomerSerializer
    def get_queryset(self):
         return Customer.objects.filter(id=self.request.user.pk)
    

class CustomerCreateAccountAPIView(generics.CreateAPIView):
    queryset=Customer.objects.all()
    serializer_class = CustomerCreateAccountSerializer
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permission checks
    
    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        # Create the provider user
        customer = serializer.save()



class CustomerAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        User = get_user_model()
        try:
            user = MyUser.objects.get(username=username)
            customer=Customer.objects.get(username=user.username)

        except User.DoesNotExist:
            return Response({'error': 'not customer account'})
        
        if check_password(password, user.password):
            if(customer.username ==user.username):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': {
                        'id': customer.id,
                        'username': customer.username,
                        'email': customer.email,
                        'phone':customer.phone,
                    }
                })
            

        return Response({'error': 'Invalid credentials'})
    
class CustomerPasswordUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomerPasswordUpdateSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        customer = self.request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        # Check if the old password is correct
        if not customer.check_password(old_password):
            return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the password
        customer.set_password(new_password)
        customer.save()

        return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)
    

class CustomerAddressRetrieveUpdateDestroyAPIView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        customer = Customer.objects.get(pk=self.request.user.id)
        return customer

    
    # def perform_update(self, serializer):
    #     customer = Customer.objects.get(pk=self.request.user.id)
    #     # serializer.partial = True
    #     serializer.save(latitude=customer.latitude, longitude=customer.longitude, address=customer.address)
########### end customer



#########  for customer views

class ProviderDataAPIView(generics.ListAPIView):
    serializer_class =ProviderSerializer
    def get_queryset(self):
         return Provider.objects.filter(id=self.request.user.pk)
    
    
class ProviderCreateAccountAPIView(generics.CreateAPIView):
    queryset=Provider.objects.all()
    serializer_class = ProviderCreateAccountSerializer
    # authentication_classes = []  # Disable authentication
    # permission_classes = []  # Disable permission checks
    
    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        # Create the provider user
        provider = serializer.save()
        provider = serializer.save()

        # Create the associated store
        store_data = {
            'provider': provider,
            # 'image': self.request.data.get('store_image'),  # Replace with the actual field name
            # 'name': self.request.data.get('store_name'),  # Replace with the actual field name
            # 'about': self.request.data.get('store_about')  # Replace with the actual field name
        }
        store_serializer = StoreForProviderWhenCreateSerializer(data=store_data)
        store_serializer.is_valid(raise_exception=True)
        store_serializer.save()
        # return Response(provider.data, status=status.HTTP_201_CREATED)



class ProviderAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        User = get_user_model()
        try:
            user = MyUser.objects.get(username=username)
            provider=Provider.objects.get(username=user.username)

        except User.DoesNotExist:
            return Response({'error': 'not provider account'})
        
        if check_password(password, user.password):
            if(provider.username ==user.username):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': {
                        'id': provider.id,
                        'username': provider.username,
                        'email': provider.email,
                        'phone':provider.phone,
                    }
                })
            

        return Response({'error': 'Invalid credentials'})
    
class ProviderPasswordUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProviderPasswordUpdateSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        provider = self.request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        # Check if the old password is correct
        if not provider.check_password(old_password):
            return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the password
        provider.set_password(new_password)
        provider.save()

        return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)
    

class ProviderAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        provider = Provider.objects.get(pk=self.request.user.id)
        return provider
########### end customer