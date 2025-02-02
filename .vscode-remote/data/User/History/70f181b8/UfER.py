from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
import uuid

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
        # Use email as the username
        self.fields['email'].widget.attrs.update({'autofocus': True})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = f"{self.cleaned_data['email']}_{uuid.uuid4().hex[:6]}"
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, mobile=self.cleaned_data['mobile'])
        return user