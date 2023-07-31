from django.urls import path
from .import views

urlpatterns = [
    path('crops/', views.PlantListView.as_view(), name='crop_list'),
    path('crops/<int:pk>/', views.PlantDetailView.as_view(), name='crop_detail')
]