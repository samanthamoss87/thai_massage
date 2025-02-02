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

class TreatmentsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Treatments.objects.create(
            title="Thai Massage",
            description="A traditional Thai massage to relax your body and mind.",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_title_label(self):
        # Test the title field label
        treatment = Treatments.objects.get(id=1)
        field_label = treatment._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        # Test the description field label
        treatment = Treatments.objects.get(id=1)
        field_label = treatment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_half_hour_default_value(self):
        # Test the default value of the half_hour field
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.half_hour, 55.00)

    def test_one_hour_default_value(self):
        # Test the default value of the one_hour field
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.one_hour, 80.00)

    def test_two_hour_default_value(self):
        # Test the default value of the two_hour field
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.two_hour, 110.00)

    def test_title_max_length(self):
        # Test the max_length of the title field
        treatment = Treatments.objects.get(id=1)
        max_length = treatment._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_title(self):
        # Test the __str__ method of the model
        treatment = Treatments.objects.get(id=1)
        expected_object_name = treatment.title
        self.assertEqual(str(treatment), expected_object_name)
