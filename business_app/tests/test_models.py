from django.test import TestCase
from business_app.models import Session

class SessionModelTestCase(TestCase):
    def setUp(self):
        # Create sample Session instances for testing
        self.session1 = Session.objects.create(name="Sample Session 1", length="60", price=50, is_active=True)
        self.session2 = Session.objects.create(name="Sample Session 2", length="45", price=40, is_active=False)

    def test_session_str_representation(self):
        """Test the __str__ method of Session model."""
        self.assertEqual(str(self.session1), "Sample Session 1")
        self.assertEqual(str(self.session2), "Sample Session 2")

    def test_session_absolute_url(self):
        """Test the get_absolute_url method of Session model."""
        expected_url = f"/session/{self.session1.id}"  # Adjust the URL pattern as needed
        self.assertEqual(self.session1.get_absolute_url(), expected_url)


