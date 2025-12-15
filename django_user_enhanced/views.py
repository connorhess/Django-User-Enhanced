"""
Authentication views for Django User Enhanced
"""
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import (
    EnhancedUserCreationForm,
    EnhancedAuthenticationForm,
    EnhancedPasswordResetForm,
    EnhancedSetPasswordForm
)


class EnhancedLoginView(LoginView):
    """Enhanced login view with custom template and form"""
    template_name = 'django_user_enhanced/login.html'
    form_class = EnhancedAuthenticationForm
    redirect_authenticated_user = True


class EnhancedLogoutView(LogoutView):
    """Enhanced logout view"""
    next_page = 'django_user_enhanced:login'


class EnhancedRegisterView(CreateView):
    """Enhanced registration view"""
    template_name = 'django_user_enhanced/register.html'
    form_class = EnhancedUserCreationForm
    success_url = reverse_lazy('django_user_enhanced:login')


class EnhancedPasswordResetView(PasswordResetView):
    """Enhanced password reset view"""
    template_name = 'django_user_enhanced/password_reset.html'
    form_class = EnhancedPasswordResetForm
    success_url = reverse_lazy('django_user_enhanced:password_reset_done')
    email_template_name = 'django_user_enhanced/password_reset_email.html'


class EnhancedPasswordResetDoneView(PasswordResetDoneView):
    """Enhanced password reset done view"""
    template_name = 'django_user_enhanced/password_reset_done.html'


class EnhancedPasswordResetConfirmView(PasswordResetConfirmView):
    """Enhanced password reset confirm view"""
    template_name = 'django_user_enhanced/password_reset_confirm.html'
    form_class = EnhancedSetPasswordForm
    success_url = reverse_lazy('django_user_enhanced:password_reset_complete')


class EnhancedPasswordResetCompleteView(PasswordResetCompleteView):
    """Enhanced password reset complete view"""
    template_name = 'django_user_enhanced/password_reset_complete.html'


@method_decorator(login_required, name='dispatch')
class EnhancedProfileView(TemplateView):
    """Enhanced user profile view"""
    template_name = 'django_user_enhanced/profile.html'
