from django.contrib import admin
from .views import index
from django.urls import include, path

urlpatterns = [
    path('', include('user_profiles.urls')),
    path('admin',admin.site.urls),
    path('', index)
]
