from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from .models import UserProfile, Booking

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': True})

    def save(self, commit=True):
        user = super().save(commit=False)
        # Generate username from first name and last name
        base_username = f"{self.cleaned_data['first_name'].lower()}_{self.cleaned_data['last_name'].lower()}"
        username = base_username
        # Ensure the username is unique
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}_{uuid.uuid4().hex[:4]}"  # Append a unique identifier
            counter += 1
        user.username = username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user, mobile=self.cleaned_data['mobile'])
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'autofocus': True}),
        label="Email Address"
    )


# Treatment booking Form
class BookingForm(forms.ModelForm):
    DURATION_CHOICES = [
        (30, '30 Minutes - $55'),
        (60, '60 Minutes - $80'),
        (120, '120 Minutes - $110'),
    ]

    duration = forms.ChoiceField(choices=DURATION_CHOICES, widget=forms.RadioSelect)
    start_time = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ['treatment', 'date', 'start_time', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'treatment': forms.Select(attrs={"class": 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate time slots from 9 AM to 10 PM in 30-minute intervals
        self.fields['start_time'].choices = self.generate_time_slots()

    def generate_time_slots(self):
        time_slots = []
        start_time = datetime.time(9, 0)  # 9:00 AM
        end_time = datetime.time(22, 0)   # 10:00 PM
        delta = datetime.timedelta(minutes=30)  # 30-minute intervals

        current_time = datetime.datetime.combine(datetime.date.today(), start_time)
        end_datetime = datetime.datetime.combine(datetime.date.today(), end_time)

        while current_time <= end_datetime:
            time_slots.append((current_time.time().strftime('%H:%M'), current_time.strftime('%I:%M %p')))
            current_time += delta

        return time_slots

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        duration = int(cleaned_data.get('duration', 0))

        if date and start_time and duration:
            # Convert start_time string to time object
            start_time = datetime.datetime.strptime(start_time, '%H:%M').time()

            # Calculate end time
            start_dt = datetime.datetime.combine(date, start_time)
            end_dt = start_dt + datetime.timedelta(minutes=duration)
            
            # Check existing bookings
            conflicts = Booking.objects.filter(
                date=date,
                start_time__lt=end_dt.time(),
                end_time__gt=start_dt.time()
            )
            if conflicts.exists():
                raise ValidationError("This time slot is already booked")

        return cleaned_data
