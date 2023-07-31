from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import UserSerializer

# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
