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
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.authentication import TokenAuthentication
from provider_details.serializers import StoreForProviderWhenCreateSerializer
from rest_framework.views import APIView

def error_handler(e):
    error_messages = {}
    for field, errors in e.items():
        error_messages["error"] = "("+field+ ") " + errors[0]
    return error_messages

# Create your views here.
def redirect_to_admin(request):
    return HttpResponseRedirect(reverse("admin:login"))


#########  for customer views

class CustomerDataAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get_object(self):
        return self.queryset.get(id=self.request.user.pk)

# class CustomerCreateAccountAPIView(generics.CreateAPIView):
#     queryset=Customer.objects.all()
#     serializer_class = CustomerCreateAccountSerializer
#     authentication_classes = []  # Disable authentication
#     permission_classes = []  # Disable permission checks
    
#     def perform_create(self, serializer):
#         try:
#             serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
#             # Create the provider user
#             customer = serializer.save()
#         except ValidationError as e: 
#             error=error_handler(e)
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
class CustomerCreateAccountAPIView(APIView):
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permission checks
    def post(self, request):
        try:
            serializer = CustomerCreateAccountSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
             return Response(error_handler(serializer.errors), status=status.HTTP_400_BAD_REQUEST)



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
        
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            customer = self.request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
        except:
             return Response(error_handler(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

        # Check if the old password is correct
        if not customer.check_password(old_password):
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

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
from django.http import HttpResponse

class ProviderDataAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProviderSerializer

    def get_object(self):
        return Provider.objects.get(id=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return HttpResponse(serializer.data, content_type='application/json; charset=utf-8')
    
class ProviderCreateAccountAPIView(generics.CreateAPIView):
    queryset=Provider.objects.all()
    serializer_class = ProviderCreateAccountSerializer
    # authentication_classes = []  # Disable authentication
    # permission_classes = []  # Disable permission checks
    
    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        # Create the provider user
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
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        User = get_user_model()
        try:
            user = MyUser.objects.get(username=username)
            provider=Provider.objects.get(username=user.username)

        except User.DoesNotExist:
            return Response({'error': 'not provider account'}, status=status.HTTP_400_BAD_REQUEST)
        
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
            

        return Response({'error': 'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
    
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        provider = Provider.objects.get(pk=self.request.user.id)
        return provider
########### end customer
class ProviderInfoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderInfoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        provider = Provider.objects.get(pk=self.request.user.id)
        return provider