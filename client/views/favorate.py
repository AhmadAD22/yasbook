from rest_framework.response import Response
from rest_framework.views import APIView
from provider_details.models import Service
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from ..serializers.favorate import *

from auth_login.models import Customer
from ..models import FavorateService

class FavoriteAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        # Get the customer from the request
        customer = Customer.objects.get(phone=request.user.phone)

        # Get the favorite products and services for the customer
        favorite_products = FavorateProduct.objects.filter(customer=customer)
        favorite_services = FavorateService.objects.filter(customer=customer)

        # Serialize the data
        product_serializer = FavorateProductSerializer(favorite_products, many=True,context={'request': request})
        service_serializer =FavorateServiceSerializer (favorite_services, many=True,context={'request': request})

        # Combine the data and return it
        data = {
            'favorite_products': product_serializer.data,
            'favorite_services': service_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)