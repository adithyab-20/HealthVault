from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            D_username = form.cleaned_data.get('D_username')
    else:
        form = UserCreationForm()
    return render(request, 'Doctor_login.html', {'form': form})

def Doctor_Personal_Information(request):
    context = {}
    if request.method == 'POST':
        form = DoctorPersonalInformation(request.POST)
        if form.is_valid():
            form.save()
            Doctor_fullname = form.cleaned_data.get('full_Name')
            Doctor_id = form.cleaned_data.get('Doctor_ID')
            Doctor_specialization = form.cleaned_data.get('Specialization')
            Doctor_education = form.cleaned_data.get('Education')
            Doctor_overview = form.cleaned_data.get('Overview')
            Doctor_experience = form.cleaned_data.get('Work_Experience')
            messages.success(request, f'Doctor Personal Information Form submitted by {Doctor_fullname}!')

        else:
            context['form'] = form
    else:
        form = form
        context['form'] = form
    return render(request, 'Doctor_Information.html', context)