from ..serializers.store import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from provider_details.models import Store

class StoreDetailView(APIView):
    """
    Retrieve a store instance.
    """
    def get(self, request, pk):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreADetailSerializer(store)
        return Response(serializer.data)

    # You can also add other HTTP methods like post, put, delete, etc.
    # as needed for your use case.