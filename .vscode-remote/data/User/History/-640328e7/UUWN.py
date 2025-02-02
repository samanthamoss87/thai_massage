from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
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
    return render(request, 'booking.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Login Page
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                print("Login Successfully")
                return redirect('dashboard')  # Redirect to the dashboard after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    return render(request, 'dashboard.html')

# Register Page
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user created")
            # Log the user in
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})