from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
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
    class Meta:
        model = Booking
        fields = ['treatment', 'duration' 'date', 'time', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the minimum date to today
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()})
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})