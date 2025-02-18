from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, time, timedelta
from .forms import UserRegisterForm, BookingForm
from .models import Treatments, UserProfile, Booking


class BookingViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_treatments_page(self):
        response = self.client.get(reverse('treatments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'treatments.html')

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
        Treatments.objects.create(
            title="Thai Massage",
            description="A traditional Thai massage to relax your body and mind.",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_title_label(self):
        treatment = Treatments.objects.get(id=1)
        field_label = treatment._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        treatment = Treatments.objects.get(id=1)
        field_label = treatment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_half_hour_default_value(self):
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.half_hour, 55.00)

    def test_one_hour_default_value(self):
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.one_hour, 80.00)

    def test_two_hour_default_value(self):
        treatment = Treatments.objects.get(id=1)
        self.assertEqual(treatment.two_hour, 110.00)

    def test_title_max_length(self):
        treatment = Treatments.objects.get(id=1)
        max_length = treatment._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_title(self):
        treatment = Treatments.objects.get(id=1)
        expected_object_name = treatment.title
        self.assertEqual(str(treatment), expected_object_name)



class UserRegisterFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_username_generation(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(user.username.startswith('john_doe'))


    def test_unique_username(self):
        form_data1 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form1 = UserRegisterForm(data=form_data1)
        self.assertTrue(form1.is_valid())
        user1 = form1.save()

        form_data2 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe2@example.com',
            'mobile': '0987654321',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form2 = UserRegisterForm(data=form_data2)
        self.assertTrue(form2.is_valid())
        user2 = form2.save()

        self.assertNotEqual(user1.username, user2.username)
        self.assertTrue(user2.username.startswith('john_doe_'))

    def test_user_profile_creation(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()

        self.assertTrue(hasattr(user, 'userprofile'))
        self.assertEqual(user.userprofile.mobile, '1234567890')


class NavbarTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User'
        )
        self.client = Client()

    def test_navbar_for_authenticated_user(self):
        self.client.login(username='testuser@example.com', password='testpassword123')

        response = self.client.get(reverse('home'))

        self.assertContains(response, 'Welcome, Test!')
        self.assertContains(response, reverse('logout'))
        self.assertNotContains(response, reverse('login'))


    def test_navbar_for_unauthenticated_user(self):
        response = self.client.get(reverse('home'))

        self.assertContains(response, reverse('login'))
        self.assertNotContains(response, 'Welcome, Test!')
        self.assertNotContains(response, reverse('logout'))


class TreatmentsModelTest(TestCase):
    def setUp(self):
        self.treatment = Treatments.objects.create(
            title='Deep Tissue Massage',
            description='A deep tissue massage to relieve muscle tension.',
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_treatment_creation(self):
        self.assertEqual(self.treatment.title, 'Deep Tissue Massage')
        self.assertEqual(self.treatment.description, 'A deep tissue massage to relieve muscle tension.')
        self.assertEqual(self.treatment.half_hour, 55.00)
        self.assertEqual(self.treatment.one_hour, 80.00)
        self.assertEqual(self.treatment.two_hour, 110.00)

    def test_treatment_str_representation(self):
        self.assertEqual(str(self.treatment), 'Deep Tissue Massage')


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.treatment = Treatments.objects.create(
            title='Swedish Massage',
            description='A relaxing full-body massage.',
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user,
            treatment=self.treatment,
            date=date(2023, 10, 25),
            start_time=time(14, 0),
            duration=60
        )

        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.treatment, self.treatment)
        self.assertEqual(booking.date, date(2023, 10, 25))
        self.assertEqual(booking.start_time, time(14, 0))
        self.assertEqual(booking.duration, 60)
        self.assertEqual(booking.end_time, time(15, 0))

    def test_booking_str_representation(self):
        booking = Booking.objects.create(
            user=self.user,
            treatment=self.treatment,
            date=date(2023, 10, 25),
            start_time=time(14, 0),
            duration=60
        )

        expected_str = "testuser - Swedish Massage on 2023-10-25 at 14:00:00 for 60 minutes"
        self.assertEqual(str(booking), expected_str)

    def test_booking_save_method(self):
        booking = Booking(
            user=self.user,
            treatment=self.treatment,
            date=date(2023, 10, 25),
            start_time=time(14, 0),
            duration=90
        )
        booking.save()

        self.assertEqual(booking.end_time, time(15, 30))
