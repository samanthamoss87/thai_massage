from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']