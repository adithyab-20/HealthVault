import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Doctor.models import Doctor_latest_diagnosis
from django.forms import ModelForm
from django.contrib.auth.forms import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import Form

class LatestDiagnosisForm(ModelForm):

    Patient_name = forms.CharField(label='Full name',max_length=100)
    Doctor_name = forms.CharField(label='Patient name',max_length=100)
    Patient_ID = forms.IntegerField()
    Doctor_ID = forms.IntegerField()
    Department = forms.CharField(label='Department',max_length=100)
    # Date_of_updation = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateInput(
    #        attrs={
    #             'type': 'date', 
    #             'class': 'form_input',
    #        },
    #     ),
    # )
    Diagnosis = forms.CharField(widget=forms.Textarea)
    Diagnosis_description = forms.CharField(widget=forms.Textarea)
    Doctor_advice = forms.CharField(widget=forms.Textarea)
    Additional_comments = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Doctor_latest_diagnosis
        fields = ("Patient_name", "Doctor_name", "Patient_ID", "Doctor_ID", "Department", "Diagnosis", "Diagnosis_description", "Doctor_advice", "Additional_comments",)
        widgets = {
            'text': forms.Textarea(attrs={'rows':5, 'cols':10}), #this is changeble.
        }