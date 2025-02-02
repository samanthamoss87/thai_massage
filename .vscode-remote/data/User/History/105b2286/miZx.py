from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterForm, BookingForm
from .models import Treatments, UserProfile, Booking


# Test for Booking App's page views
class BookingViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_treatments_page(self):
        response = self.client.get(reverse('treatments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'treatments.html')

    # def test_book_now_page(self):
    #     response = self.client.get(reverse('book-now'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'booking.html')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


# Test For Treatments model
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


# Test for User Registration Form
class UserRegisterFormTest(TestCase):
    def test_form_valid(self):
        # Test valid form submission
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
        # Test invalid form submission (missing required fields)
        form_data = {
            'first_name': '',  # Missing first name
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'mobile': '1234567890',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)  # Check for first name error

    def test_username_generation(self):
        # Test username generation from first name and last name
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
        self.assertTrue(user.username.startswith('john_doe'))  # Check username format

    def test_unique_username(self):
        # Test username uniqueness when the same name is used multiple times
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

        # Check that usernames are unique
        self.assertNotEqual(user1.username, user2.username)
        self.assertTrue(user2.username.startswith('john_doe_'))  # Check for unique suffix

    def test_user_profile_creation(self):
        # Test that UserProfile is created with the correct mobile number
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

        # Check that UserProfile is created
        self.assertTrue(hasattr(user, 'userprofile'))
        self.assertEqual(user.userprofile.mobile, '1234567890')


# Navbar Test
class NavbarTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser@example.com',  # Use email as username
            email='testuser@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User'
        )
        self.client = Client()

    def test_navbar_for_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser@example.com', password='testpassword123')

        # Access a page (e.g., home page)
        response = self.client.get(reverse('home'))

        # Check that the navbar displays the welcome message and logout link
        self.assertContains(response, 'Welcome, Test!')  # Check for welcome message
        self.assertContains(response, reverse('logout'))  # Check for logout link
        self.assertNotContains(response, reverse('login'))  # Ensure login link is not displayed

    def test_navbar_for_unauthenticated_user(self):
        # Access a page (e.g., home page) without logging in
        response = self.client.get(reverse('home'))

        # Check that the navbar displays the login link
        self.assertContains(response, reverse('login'))  # Check for login link
        self.assertNotContains(response, 'Welcome, Test!')  # Ensure welcome message is not displayed
        self.assertNotContains(response, reverse('logout'))  # Ensure logout link is not displayed

# Test for treatments model
class TreatmentsModelTest(TestCase):
    def setUp(self):
        # Create a test treatment
        self.treatment = Treatments.objects.create(
            title='Deep Tissue Massage',
            description='A deep tissue massage to relieve muscle tension.',
            half_hour=55.00,
            one_hour=80.00,
            two_hour=110.00
        )

    def test_treatment_creation(self):
        # Test that the treatment was created correctly
        self.assertEqual(self.treatment.title, 'Deep Tissue Massage')
        self.assertEqual(self.treatment.description, 'A deep tissue massage to relieve muscle tension.')
        self.assertEqual(self.treatment.half_hour, 55.00)
        self.assertEqual(self.treatment.one_hour, 80.00)
        self.assertEqual(self.treatment.two_hour, 110.00)

    def test_treatment_str_representation(self):
        # Test the __str__ method
        self.assertEqual(str(self.treatment), 'Deep Tissue Massage')