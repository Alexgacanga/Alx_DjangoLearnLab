from django.test import TestCase
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserModelTest(TestCase):
    """
    Test cases for the CustomUser model.
    """
    
    def setUp(self):
        """Set up test user instances."""
        self.user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
        }
    
    def test_create_user(self):
        """Test creating a regular user."""
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        """Test creating a superuser."""
        superuser = CustomUser.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='adminpass123',
        )
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
    
    def test_user_with_date_of_birth(self):
        """Test creating a user with date of birth."""
        from datetime import date
        user_data = self.user_data.copy()
        user_data['date_of_birth'] = date(1990, 5, 15)
        user = CustomUser.objects.create_user(**user_data)
        self.assertEqual(user.date_of_birth, date(1990, 5, 15))
    
    def test_email_unique(self):
        """Test that email field is unique."""
        CustomUser.objects.create_user(**self.user_data)
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(**self.user_data)
    
    def test_user_str(self):
        """Test the string representation of a user."""
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), 'testuser@example.com')
