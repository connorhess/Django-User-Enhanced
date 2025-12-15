"""
URL configuration for myproject example.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django_user_enhanced.urls')),  # Django User Enhanced URLs
    path('', views.home, name='home'),
]
