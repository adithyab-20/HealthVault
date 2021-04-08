import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Patient.models import Account
from django.forms import ModelForm
from django.contrib.auth.forms import forms
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
    DOB = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateInput(
           attrs={
                'type': 'date', 
                'class': 'form_input',
           },
        ),
    )
    Age = forms.IntegerField()
    Gender = forms.CharField(max_length=20)
    Height = forms.IntegerField(label='in cm')
    Weight = forms.IntegerField(label='in kg')
    Blood_Group =  forms.CharField(max_length=5)
    Alchohol_Consumption = forms.CharField(max_length=50)
    Smoking_Habit = forms.CharField(max_length=50)
    Drug_Allergies = forms.CharField(widget=forms.Textarea)
    Current_Medications = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Patient_medical_history
        fields = ("Full_name", "DOB", "Age", "Gender", "Height", "Weight", "Blood_Group", "Alchohol_Consumption", "Smoking_Habit", "Drug_Allergies", "Current_Medications",)
        widgets = {
            'text': forms.Textarea(attrs={'rows':5, 'cols':10}), #this is changeble.
        }

#date-time code for to insert into html template
# {{ form.date.id_for_label }}
# <script>
#   $(function () {
#     $("#{{ form.date.id_for_label }}").datetimepicker({
#       format: 'd/m/Y H:i',
#     });
#   });
# </script>