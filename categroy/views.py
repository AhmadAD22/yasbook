from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes=[]
    permission_classes = []


class MainServiceListView(generics.ListAPIView):

    serializer_class = MainServiceSerializer
    authentication_classes=[]
    permission_classes = []

    def get_queryset(self):
        category_id = self.kwargs['category_id']  # Get the university_id from URL
        return MainService.objects.filter(category_id=category_id)