from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import views

from .views import UserLoginAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='long'),
    path('api-token-auth/', views.obtain_auth_token)
]