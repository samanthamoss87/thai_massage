from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import time, timedelta, datetime

from .forms import UserRegisterForm, BookingForm, UserLoginForm, ContactForm
from .models import Treatments, UserProfile, Booking, Contact


""" Testing Pages """


class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class TreatmentsPageTest(TestCase):
    def setUp(self):
        Treatments.objects.create(
            title="Massage Therapy",
            description="Relaxing massage",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )
        Treatments.objects.create(
            title="Facial Therapy",
            description="Skin care treatment",
            half_hour=50.00,
            one_hour=75.00,
            two_hour=100.00
        )

    def test_treatments_page_status_code(self):
        response = self.client.get(reverse('treatments'))
        self.assertEqual(response.status_code, 200)

    def test_treatments_page_template(self):
        response = self.client.get(reverse('treatments'))
        self.assertTemplateUsed(response, 'treatments.html')

    def test_treatments_displayed_in_template(self):
        response = self.client.get(reverse('treatments'))
        self.assertContains(response, "Massage Therapy")
        self.assertContains(response, "Facial Therapy")


class ContactPageTest(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact.html')


class LoginPageTest(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')


class BookNowPageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.treatment = Treatments.objects.create(
            title="Massage Therapy",
            description="Relaxing massage",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_book_now_page_status_code_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('book_now'))
        self.assertEqual(response.status_code, 200)

    def test_book_now_page_status_code_unauthenticated(self):
        response = self.client.get(reverse('book_now'))
        self.assertRedirects(response, '/login/?next=/book-now/')


class BookingSuccessPageTest(TestCase):
    def test_booking_success_page_status_code(self):
        response = self.client.get(reverse('booking_success'))
        self.assertEqual(response.status_code, 200)

    def test_booking_success_page_template(self):
        response = self.client.get(reverse('booking_success'))
        self.assertTemplateUsed(response, 'booking_success.html')


""" Testing Models """


class TreatmentsModelTest(TestCase):

    def test_treatment_creation(self):
        treatment = Treatments.objects.create(
            title="Massage Therapy",
            description="Relaxing massage for stress relief",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )
        self.assertEqual(treatment.title, "Massage Therapy")
        self.assertEqual(
            treatment.description,
            "Relaxing massage for stress relief"
        )
        self.assertEqual(treatment.half_hour, 55.00)
        self.assertEqual(treatment.one_hour, 80.00)
        self.assertEqual(treatment.two_hour, 110.00)
        self.assertTrue(treatment.id)


class UserProfileModelTest(TestCase):

    def test_user_profile_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        user_profile = UserProfile.objects.create(
            user=user,
            mobile="1234567890"
        )

        self.assertEqual(user_profile.user.username, 'testuser')
        self.assertEqual(user_profile.mobile, "1234567890")
        self.assertTrue(user_profile.id)


class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.treatment = Treatments.objects.create(
            title="Massage Therapy",
            description="Relaxing massage for stress relief",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user,
            treatment=self.treatment,
            date=datetime.strptime('2025-06-30', '%Y-%m-%d').date(),
            start_time=time(10, 0),
            duration=60
        )

        self.assertEqual(booking.user.username, 'testuser')
        self.assertEqual(booking.treatment.title, 'Massage Therapy')
        self.assertEqual(booking.duration, 60)

        expected_end_time = (datetime.combine(
            booking.date,
            booking.start_time
        ) + timedelta(minutes=booking.duration)).time()
        self.assertEqual(booking.end_time, expected_end_time)

    def test_booking_duration_update(self):
        booking = Booking.objects.create(
            user=self.user,
            treatment=self.treatment,
            date=datetime.strptime('2025-06-30', '%Y-%m-%d').date(),
            start_time=time(10, 0),
            duration=60
        )

        booking.duration = 90
        booking.save()

        expected_end_time = (datetime.combine(
            booking.date,
            booking.start_time
        ) + timedelta(minutes=booking.duration)).time()
        self.assertEqual(booking.end_time, expected_end_time)


class ContactModelTest(TestCase):

    def test_contact_creation(self):
        contact = Contact.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            subject="Inquiry",
            message="Hello, I would like to inquire about your services."
        )

        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "john.doe@example.com")
        self.assertEqual(contact.subject, "Inquiry")
        self.assertEqual(
            contact.message,
            "Hello, I would like to inquire about your services."
        )
        self.assertTrue(contact.created_at)


""" Testing forms """


class UserRegisterFormTest(TestCase):

    def test_user_register_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'Str0ngP@ssw0rd!',
            'password2': 'Str0ngP@ssw0rd!',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

        user = form.save(commit=False)
        user.save()

        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(
            get_user_model().objects.first().email,
            'john.doe@example.com'
        )


class UserLoginFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='johndoe@gmail.com',
            password='Str0ngP@ssw0rd!'
        )

    def test_user_login_form_valid(self):
        form_data = {
            'username': 'johndoe@gmail.com',
            'password': 'Str0ngP@ssw0rd!',
        }
        form = UserLoginForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())


class BookingFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='12345'
        )
        self.treatment = Treatments.objects.create(
            title="Massage Therapy",
            description="Relaxing massage for stress relief",
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_booking_form_valid(self):
        form_data = {
            'treatment': self.treatment.id,
            'date': '2025-06-30',
            'start_time': '10:00',
            'duration': 60
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

        booking = form.save(commit=False)
        booking.user = self.user
        booking.save()

        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().start_time, time(10, 0))
        self.assertEqual(Booking.objects.first().duration, 60)


class ContactFormTest(TestCase):

    def test_contact_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'subject': 'Inquiry',
            'message': 'Hello, I would like to inquire about your services.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

        form.save()
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'john.doe@example.com')
        self.assertEqual(contact.subject, 'Inquiry')
        self.assertEqual(
            contact.message,
            'Hello, I would like to inquire about your services.'
        )
