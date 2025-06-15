from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import UserRegisterForm, UserLoginForm, BookingForm, ContactForm
from .models import Treatments, Booking


def home(request):
    return render(request, 'home.html')


def treatments(request):
    treatment_list = Treatments.objects.all()
    return render(request, 'treatments.html', {'treatments': treatment_list})


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


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'edit_booking.html',
        {'form': form, 'booking': booking}
    )


def booking_success(request):
    return render(request, 'booking_success.html')


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user == request.user:
        booking.delete()
        from django.contrib import messages
        messages.success(
            request,
            'Your booking has been canceled successfully.'
        )
    else:
        messages.error(
            request,
            'You do not have permission to cancel this booking.'
        )
    return redirect('dashboard')


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


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='booking.backends.EmailAuthBackend')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid email or password.")
        else:
            form.add_error(None, "Please correct the errors below.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    now = timezone.now().date()

    future_bookings = Booking.objects.filter(
        user=request.user,
        date__gte=now
    ).order_by('date', 'start_time')

    context = {
        'future_bookings': future_bookings,
    }
    return render(request, 'dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def coming_soon(request):
    return render(request, 'coming_soon.html')


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
