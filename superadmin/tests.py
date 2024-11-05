from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import CustomUser  

# Create your tests here.


class UserAuthTests(TestCase):
    def setUp(self):
        # Set up a test user
        self.user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'raw_password': 'testpassword',
            'cu_role': 'vendor',  # Adjust this according to your RoleModel setup
        }

    def test_registration(self):
        # Test user registration
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after registration
        self.assertTrue(CustomUser.objects.filter(email='testuser@example.com').exists())  # Check if user is created

    def test_login(self):
        # First register the user
        self.client.post(reverse('register'), self.user_data)

        # Test user login
        response = self.client.post(reverse('login'), {
            'email': 'testuser@example.com',
            'raw_password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful login
        self.assertIn('_auth_user_id', self.client.session)  # Check if the user is logged in

    def test_login_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {
            'email': 'wronguser@example.com',
            'raw_password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Expect to stay on the login page
        self.assertNotIn('_auth_user_id', self.client.session)  # User should not be logged in



