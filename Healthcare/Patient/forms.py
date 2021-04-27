import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Patient.models import Account, Patient_medical_history
from django.forms import ModelForm
from django.contrib.auth.forms import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import Form


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(max_length=60, help_text="Required. Please add a valid email address")
    full_name = forms.CharField(max_length=100, help_text="Full Name")
    USERNAME_FIELD = 'email'
    
    class Meta:
        model = Account
        fields = ("full_name", "email", "password1", "password2",)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_id = 'id-SignupForm'

        for fieldname in ['full_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.helper.add_input(Submit('signup', 'Click to Signup!', css_id='ajax_save', css_class='submit'))




class MedicalHistoryForm(ModelForm):

    Full_name = forms.CharField(label='Full name',max_length=100)
    # DOB = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateInput(
    #        attrs={
    #             'type': 'date', 
    #             'class': 'form_input',
    #        },
    #     ),
    # )
    Age = forms.IntegerField()
    Gender = forms.CharField(max_length=20)
    Height = forms.IntegerField(label='Height(in cm)')
    Weight = forms.IntegerField(label='Weight(in kg)')
    Blood_Group =  forms.CharField(max_length=5)
    Alchohol_Consumption = forms.CharField(max_length=50)
    Smoking_Habit = forms.CharField(max_length=50)
    Drug_Allergies = forms.CharField(widget=forms.Textarea)
    Current_Medications = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Patient_medical_history
        fields = ("Full_name", "Age", "Gender", "Height", "Weight", "Blood_Group", "Alchohol_Consumption", "Smoking_Habit", "Drug_Allergies", "Current_Medications",)
        widgets = {
            'text': forms.Textarea(attrs={'rows':5, 'cols':10}), #this is changeble.
        }


# {{ form.date.id_for_label }}
# <script>
#   $(function () {
#     $("#{{ form.date.id_for_label }}").datetimepicker({
#       format: 'd/m/Y H:i',
#     });
#   });
# </script>