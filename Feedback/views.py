from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import FeedbackSerializer

# Create your views here.
class FeedbackListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = FeedbackSerializer