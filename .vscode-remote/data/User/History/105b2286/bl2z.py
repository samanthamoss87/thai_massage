from django.test import TestCase
from django.urls import reverse



class BookingViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_treatments_page(self):
        response = self.client.get(reverse('treatments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'treatments.html')

    def test_book_now_page(self):
        response = self.client.get(reverse('book_now'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_now.html')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')



class TreatmentsModelTestCase(TestCase):
    def setUp(self):
        """Create a test service before each test."""
        self.service = Service.objects.create(
            title="Thai Classic Massage",
            description="A traditional Thai massage using stretching techniques.",
        )

    def test_service_creation(self):
        """Test if the service is created properly."""
        self.assertEqual(self.service.title, "Thai Classic Massage")
        self.assertEqual(self.service.description, "A traditional Thai massage using stretching techniques.")

    def test_service_default_prices(self):
        """Test if default prices are correctly set."""
        self.assertEqual(self.service.half_hour, 55.00)
        self.assertEqual(self.service.one_hour, 80.00)
        self.assertEqual(self.service.two_hour, 110.00)

    def test_service_str_method(self):
        """Test the __str__ method returns the title."""
        self.assertEqual(str(self.service), "Thai Classic Massage")