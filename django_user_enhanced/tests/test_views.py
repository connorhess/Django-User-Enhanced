"""
Tests for Django User Enhanced views
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationViewsTestCase(TestCase):
    """Test cases for authentication views"""
    
    def setUp(self):
        """Set up test client and test user"""
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_login_view_get(self):
        """Test login view GET request"""
        response = self.client.get(reverse('django_user_enhanced:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_user_enhanced/login.html')
    
    def test_login_view_post_success(self):
        """Test successful login"""
        response = self.client.post(
            reverse('django_user_enhanced:login'),
            {'username': 'testuser', 'password': 'testpass123'},
            follow=True
        )
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    
    def test_login_view_post_failure(self):
        """Test failed login with wrong credentials"""
        response = self.client.post(
            reverse('django_user_enhanced:login'),
            {'username': 'testuser', 'password': 'wrongpassword'}
        )
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    
    def test_register_view_get(self):
        """Test register view GET request"""
        response = self.client.get(reverse('django_user_enhanced:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_user_enhanced/register.html')
    
    def test_register_view_post_success(self):
        """Test successful user registration"""
        user_count_before = User.objects.count()
        response = self.client.post(
            reverse('django_user_enhanced:register'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'newpass123!',
                'password2': 'newpass123!'
            }
        )
        self.assertEqual(User.objects.count(), user_count_before + 1)
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_profile_view_requires_login(self):
        """Test that profile view requires authentication"""
        response = self.client.get(reverse('django_user_enhanced:profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_profile_view_authenticated(self):
        """Test profile view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('django_user_enhanced:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_user_enhanced/profile.html')
    
    def test_password_reset_view_get(self):
        """Test password reset view GET request"""
        response = self.client.get(reverse('django_user_enhanced:password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_user_enhanced/password_reset.html')
    
    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='testuser', password='testpass123')
        # Verify user is logged in
        response = self.client.get(reverse('django_user_enhanced:profile'))
        self.assertEqual(response.status_code, 200)
        
        # Logout using POST (required in Django 6.0+)
        self.client.post(reverse('django_user_enhanced:logout'))
        
        # Try to access profile again - should redirect to login
        response = self.client.get(reverse('django_user_enhanced:profile'))
        self.assertEqual(response.status_code, 302)  # Redirected because not authenticated
