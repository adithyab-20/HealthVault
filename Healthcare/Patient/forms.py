import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Patient.models import Account
from django.forms import ModelForm
from django.contrib.auth.forms forms
from Patient.models import Patient_medical_history


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(max_length=60, help_text="Required. Please add a valid email address")
    full_name = forms.CharField(max_length=100, help_text="Full Name")
    USERNAME_FIELD = 'email'
    class Meta:
        model = Account
        fields = ("full_name", "email", "password1", "password2",)

class PatientMedicalHistoryForm(forms.Form):

    Full_name = forms.CharField(label='Full name',max_length=100)
    DOB = forms.DateField(initial=datetime.date.now, format=('%d-%m-%Y'))
    Age = forms.IntegerField()
    Gender = forms.CharField(max_length=20)
    Height = forms.IntegerField(label='in cm')
    Weight = forms.IntegerField(lablel='in kg')
    Blood_Group =  forms.CharField(max_length=5)
    Alchohol_Consumption = forms.TextField()
    Smoking_Habit = forms.TextField()
    Drug_Allergies = forms.TextField()
    Current_Medications = forms.TextField()
    class Meta:
        model = Patient_medical_history
        fields("Full_name", "DOB", "Age", "Gender", "Height", "Weight", "Blood_Group", "Alchohol_Consumption", "Smoking_Habit", "Drug_Allergies", "Current_Medications",)