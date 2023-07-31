from django.urls import path
from .import views

urlpatterns = [
    path('feedback/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback_detail'),
]