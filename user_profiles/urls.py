from django.contrib import admin
from django.urls import path
from .views import user_profiles

urlpatterns = [
    path('user_profiles', user_profiles),
]
