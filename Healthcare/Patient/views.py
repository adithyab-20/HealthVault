from django.shortcuts import render
from django.contrib.auth import login, authenticate
from Patient.forms import SignupForm
from django.contrib import messages

def Signup(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_fullname = form.cleaned_data.get('full_name')
            Patient_email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=Patient_email, password=raw_password)
            login(request,account)
            messages.success(request, f'Account created for {Patient_fullname}!')

        else:
            context['signup_form'] = form
    else:
        form = SignupForm()
        context['signup_form'] = form
    return render(request, 'Patient_Signup.html', context)

def Login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            P_username = form.cleaned_data.get('P_username')
    else:
        form = UserCreationForm()
    return render(request, 'Patient_Signup.html', {'form': form})


def Pat(request):
    return render(request, 'Patient_Signup.html')

def Medical_History_Entry(request):
    context = {}
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_Fullname = form.cleaned_data.get('Full_name')
            Patient_DateofBirth = form.cleaned_data.get('DOB')
            Patient_age = form.cleaned_data.get('Age')
            Patient_gender = form.cleaned_data.get('Gender')
            Patient_height = form.cleaned_data.get('Height')
            Patient_weight = form.cleaned_data.get('Weight')
            Patient_bloodgroup = form.cleaned_data.get('Blood_Group')
            Patient_alchohol = form.cleaned_data.get('Alchohol_Consumption')
            Patient_smoking = form.cleaned_data.get('Smoking_Habit')
            Patient_drugallergies = form.cleaned_data.get('Drug_Allergies')
            Patient_medications = form.cleaned_data.get('Current_Medications')
            messages.success(request, f'Medical History Form submitted by {Patient_Fullname}!')

        else:
            context['form'] = form
    else:
        form = form
        context['form'] = form
    return render(request, 'Medical_History_form.html', context)