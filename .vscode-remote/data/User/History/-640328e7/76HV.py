from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, BookingForm
from .models import Treatments, UserProfile

# Home Page
def home(request):
    return render(request, 'home.html')

# Treatments Page
def treatments(request):
    treatment_list = Treatments.objects.all()
    return render(request, 'treatments.html', {'treatments': treatment_list})

# Book Now Page
def book_now(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

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
            login(request, user, backend='')
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
        return redirect('login')  # Redirect to login if user is not authenticated
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')