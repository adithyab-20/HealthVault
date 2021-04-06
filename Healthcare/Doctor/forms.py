import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Doctor.models import Account
from django.forms import ModelForm
from django.contrib.auth.forms import forms
#from Doctor.models import Doctor_Info


class DoctorInformation(forms.Form):

    full_Name = forms.CharField(label='Full name',max_length=100)
    Doctor_ID =  forms.IntegerField()
    Specialization = forms.CharField(max_length=50)
    Education = forms.CharField(widget=forms.Textarea)
    Overview = forms.CharField(widget=forms.Textarea)
    Work_Experience = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Doctor_Info
        fields = ("full_Name", "Doctor_ID", "Specialization", "Education", "Overview", "Work_Experience",)
        widgets = {
            'text': forms.Textarea(attrs={'rows':5, 'cols':10}), #this is changeble.
        }