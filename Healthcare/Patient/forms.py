from django import forms
from django.contrib.auth.forms import UserCreationForm
from Patient.models import Account


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(max_length=60, help_text="Required. Please add a valid email address")
    full_name = forms.CharField(max_length=100, help_text="Full Name")
    USERNAME_FIELD = 'email'
    class Meta:
        model = Account
        fields = ("full_name", "email", "password1", "password2",)