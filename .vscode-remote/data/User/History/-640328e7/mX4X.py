from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, BookingForm
from .models import Treatments, UserProfile, Booking

# Home Page
def home(request):
    return render(request, 'home.html')

# Treatments Page
def treatments(request):
    treatment_list = Treatments.objects.all()
    return render(request, 'treatments.html', {'treatments': treatment_list})

# Book Now Page
@login_required
def book_now(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.duration = int(form.cleaned_data['duration'])  # Save the selected duration
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Register Page
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user created")
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
    # Get the current date/time
    now = timezone.now().date()

    # Filter bookings for the logged-in user and future dates
    future_bookings = Booking.objects.filter(
        user=request.user,  # Filter by logged-in user
        date__gte=now       # Filter future dates (greater than or equal to today)
    ).order_by('date', 'time_slot')  # Optional: Order by date and time

    # Pass the filtered bookings to the template
    context = {
        'future_bookings': future_bookings,
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')