from django.urls import path
from .import views

urlpatterns = [
    path('newcrops/', views.UserCropListView.as_view(), name='newcrop_list'),
    path('newcrop/', views.UserCropDetailView.as_view(), name='newcrop_detail')
]