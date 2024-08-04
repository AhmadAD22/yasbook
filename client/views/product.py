from rest_framework.response import Response
from rest_framework.views import APIView
from provider_details.models import Product
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from ..serializers.store import *
from ..serializers.product import *
from utils.subscriptions import active_stores
from utils.geographic import distance
from auth_login.models import Customer
from ..models import FavorateProduct


# class ServiceSearchAPIView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self, request,store_id):
#         query = request.query_params.get('query', '')
#         stores=active_stores()
#         # Get the services from the stores with active subscriptions
#         services = Service.objects.filter(store__in=stores)
#         services = services.filter(name__icontains=query)
#         serializer = ServiceListSerializer(services, many=True,context={'request': request})
#         return Response(serializer.data)


class AddproductToFavorate(APIView):
     permission_classes=[IsAuthenticated]
     def post(self,request):
         try:
            product=Product.objects.get(id=request.data['product_id'])
         except Product.DoesNotExist:
             return Response({"error": "product does not found!"}, status=status.HTTP_404_NOT_FOUND)
         customer=Customer.objects.get(phone=request.user.phone)
         try:
            favorate_product=FavorateProduct.objects.create(product=product,customer=customer)
            favorate_product.save()
         except :
             return Response({"error": "product Already Added!"}, status=status.HTTP_409_CONFLICT)
         return Response({"result":"product Adedd to favorate"},status=status.HTTP_200_OK)
     
class DeleteproductFromFavorate(APIView):
     def post(self,request):
         try:
            product=Product.objects.get(id=request.data['product_id'])
         except Product.DoesNotExist:
             return Response({"error": "product does not found!"}, status=status.HTTP_404_NOT_FOUND)
         customer=Customer.objects.get(phone=request.user.phone)
         try:
            favorate_product=FavorateProduct.objects.get(product=product,customer=customer)
            favorate_product.delete()
         except :
             return Response({"error": "product Already Deleted!"}, status=status.HTTP_409_CONFLICT)
         return Response({"result":"product deleted from favorate"},status=status.HTTP_200_OK)
     
     