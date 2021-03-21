from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_name = form.cleaned_data.get('Patient_name')
            messages.success(request, f'Account created for {Patient_name}!')
    else:
        form = UserCreationForm()
    return render(request, 'Patient_Signup.html', {'form': form})

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