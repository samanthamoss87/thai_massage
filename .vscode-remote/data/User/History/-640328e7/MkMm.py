from django.shortcuts import render

# Home Page
def home(request):
    return render(request, 'home.html')

# Treatments Page
def treatments(request):
    return render(request, 'treatments.html')

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
    return render(request, 'register.html')