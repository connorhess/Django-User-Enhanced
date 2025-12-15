"""
URL configuration for Django User Enhanced
"""
from django.urls import path
from . import views

app_name = 'django_user_enhanced'

urlpatterns = [
    path('login/', views.EnhancedLoginView.as_view(), name='login'),
    path('logout/', views.EnhancedLogoutView.as_view(), name='logout'),
    path('register/', views.EnhancedRegisterView.as_view(), name='register'),
    path('password-reset/', views.EnhancedPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.EnhancedPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.EnhancedPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.EnhancedPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.EnhancedProfileView.as_view(), name='profile'),
]
