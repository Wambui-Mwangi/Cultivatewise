from django.shortcuts import render
from rest_framework import generics
from .models import Plant
from .serializers import PlantSerializer

# Create your views here.
class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
