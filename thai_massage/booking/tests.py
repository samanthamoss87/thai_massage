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