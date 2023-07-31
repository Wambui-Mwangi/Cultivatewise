from django.shortcuts import render
from rest_framework import generics
from .models import AddedCrop
from .serializers import UserCropSerializer

# Create your views here.
class UserCropListView(generics.ListCreateAPIView):
    queryset = AddedCrop.objects.all()
    serializer_class = UserCropSerializer

class UserCropDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddedCrop.objects.all()
    serializer_class = UserCropSerializer
