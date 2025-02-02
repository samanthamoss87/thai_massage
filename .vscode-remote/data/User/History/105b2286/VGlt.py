from django.test import TestCase
from django.urls import reverse
from .models import Treatments



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
        self.assertTemplateUsed(response, 'booking.html')

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
        """Create a test treatment before each test."""
        self.treatment = Treatments.objects.create(
            title="Thai Classic Massage",
            description="A traditional Thai massage using stretching techniques.",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_treatment_creation(self):
        """Test if the treatment is created properly."""
        self.assertEqual(self.treatment.title, "Thai Classic Massage")
        self.assertEqual(self.treatment.description, "A traditional Thai massage using stretching techniques.")

    def test_treatment_prices(self):
        """Test if the prices are correctly set."""
        self.assertEqual(self.treatment.half_hour, 55.00)
        self.assertEqual(self.treatment.one_hour, 80.00)
        self.assertEqual(self.treatment.two_hour, 110.00)

    def test_treatment_str_method(self):
        """Test the __str__ method returns the title."""
        self.assertEqual(str(self.treatment), "Thai Classic Massage")