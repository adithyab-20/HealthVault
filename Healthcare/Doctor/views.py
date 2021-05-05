from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# def Login(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             D_username = form.cleaned_data.get('D_username')
#     else:
#         form = UserCreationForm()
#     return render(request, 'Doctor_login.html', {'form': form})

def Latest_Diagnosis(request):
    context = {}
    if request.method == 'POST':
        form = LatestDiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_Fullname = form.cleaned_data.get('Full_name')
            Doctor_Fullname = form.cleaned_data.get('Patient_name')
            Patient_id = form.cleaned_data.get('Patient_ID')
            Doctor_id = form.cleaned_data.get('Doctor_ID')
            Doctor_department = form.cleaned_data.get('Department')
            # Doctor_DateofUpdation = form.cleaned_data.get('Date_of_updation')
            Patient_diagnosis = form.cleaned_data.get('Diagnosis')
            Patient_diagnosis_description = form.cleaned_data.get('Diagnosis_description')
            Doctor_Advice = forms.cleaned_data.get('Doctor_advice')
            Doctor_additional_comments = form.cleaned_data.get('Additional_comments')
            return redirect('/Patient/dashboard')

        else:
            context['form'] = form
            print(form.errors)
    else:
        form = LatestDiagnosisForm()
        context['form'] = form
    return render(request, 'Latest_Diagnosis_form.html', context)