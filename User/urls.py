from django.urls import path
from .import views

urlpatterns = [
    path('user/', views.UserListView.as_view(), name='user_list'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
]