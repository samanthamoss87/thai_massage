from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
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
    return render(request, 'login.html')

# Register Page
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User created:", user)
            UserProfile.objects.create(
                user=user,
                mobile=form.cleaned_data['mobile']
            )
            print("User Profile created")
            login(request.user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})