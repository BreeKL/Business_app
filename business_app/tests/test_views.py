from django.test import TestCase, Client
from django.urls import reverse
from business_app.models import Session
from business_app.forms import SessionForm
from django.contrib.auth.models import User


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        """Test that the index view renders the correct template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_app/index.html')

class CreateSessionViewTestCase(TestCase):
    def setUp(self):
        # Create a test user (adjust username and password as needed)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_session_view(self):
        """Test that the CreateSession view correctly processes form submissions."""
        # Create a client and log in the test user
        client = Client()
        client.force_login(self.user)

        form_data = {
            'name': 'Test Session',
            'description': 'A test session',
            'length': '60',
            'price': 50,
            'is_active': True,
        }
        response = client.post(reverse('create-session'), data=form_data)

        # Check if the session was created and redirected to the sessions list
        self.assertEqual(response.status_code, 302)  # 302 is the redirect status code
        self.assertEqual(Session.objects.count(), 1)
        self.assertRedirects(response, reverse('sessions'))