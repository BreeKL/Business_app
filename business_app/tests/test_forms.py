from django.test import TestCase
from business_app.forms import SessionForm  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SessionFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Test Session',
            'description': 'A test session',
            'length': 60,
            'price': 50,
            'is_active': True,
        }
        form = SessionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test with invalid data (e.g., missing required fields)
        form = SessionForm(data={})
        self.assertFalse(form.is_valid())

class CreateUserFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test with invalid data (e.g., mismatched passwords)
        form = UserCreationForm(data={'password1': 'test1', 'password2': 'test2'})
        self.assertFalse(form.is_valid())