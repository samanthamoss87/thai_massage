from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


from .forms import UserRegisterForm, UserLoginForm, BookingForm, ContactForm
from .models import Treatments, UserProfile, Booking

# Home Page
def home(request):
    return render(request, 'home.html')

# Treatments Page
def treatments(request):
    treatment_list = Treatments.objects.all()
    return render(request, 'treatments.html', {'treatments': treatment_list})

# Book Now Page
@login_required(login_url='/login/')
def book_now(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.duration = int(form.cleaned_data['duration'])
            booking.save()
            return redirect('booking_success')

    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})

# Booking Success Page
def booking_success(request):
    return render(request, 'booking_success.html')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user == request.user:
        booking.delete()
        from django.contrib import messages
        messages.success(request, 'Your booking has been canceled successfully.')
    else:
        messages.error(request, 'You do not have permission to cancel this booking.')
    return redirect('dashboard')


# Contact Page
def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success': success})

# Register Page
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user, backend='booking.backends.EmailAuthBackend')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login Page
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Email is used as username
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                # Add an error message for invalid credentials
                form.add_error(None, "Invalid email or password.")
        else:
            # Add an error message for invalid form data
            form.add_error(None, "Please correct the errors below.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    now = timezone.now().date()

    # Filter bookings for the logged-in user and future dates
    future_bookings = Booking.objects.filter(
        user=request.user,  # Filter by logged-in user
        date__gte=now       # Filter future dates (greater than or equal to today)
    ).order_by('date', 'start_time')  # Order by date and start time

    context = {
        'future_bookings': future_bookings,
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)