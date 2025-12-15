"""
Tests for Django User Enhanced forms
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django_user_enhanced.forms import (
    EnhancedUserCreationForm,
    EnhancedAuthenticationForm,
    EnhancedPasswordResetForm
)

User = get_user_model()


class FormsTestCase(TestCase):
    """Test cases for forms"""
    
    def test_enhanced_user_creation_form_valid(self):
        """Test valid user creation form"""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123!',
            'password2': 'testpass123!'
        }
        form = EnhancedUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_enhanced_user_creation_form_password_mismatch(self):
        """Test user creation form with mismatched passwords"""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123!',
            'password2': 'differentpass123!'
        }
        form = EnhancedUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_enhanced_authentication_form_valid(self):
        """Test valid authentication form"""
        User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        form_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        form = EnhancedAuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_enhanced_password_reset_form_valid(self):
        """Test valid password reset form"""
        form_data = {
            'email': 'test@example.com'
        }
        form = EnhancedPasswordResetForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_enhanced_password_reset_form_invalid_email(self):
        """Test password reset form with invalid email"""
        form_data = {
            'email': 'invalid-email'
        }
        form = EnhancedPasswordResetForm(data=form_data)
        self.assertFalse(form.is_valid())
