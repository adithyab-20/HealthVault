from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Doctor.decorators import *
from Doctor.forms import DocProfileUpdateForm, DocImageForm
from django.contrib import messages

# def Login(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             D_username = form.cleaned_data.get('D_username')
#     else:
#         form = UserCreationForm()
#     return render(request, 'Doctor_login.html', {'form': form})


@allowed_users(allowed_roles=['Admin', 'Doctors'])
def dashboard(request):
    return render(request, 'doctor-dashboard.html')

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



def patient_redirect(request):
    return render(request, 'Patient_Redirect.html')


@login_required()
def profile(request):
    if request.method == 'POST':
        doc_form = DocProfileUpdateForm(request.POST, 
                                   instance=request.user.columbiaasia_doctor)
        
        image_form = DocImageForm(request.POST,request.FILES,instance=request.user.columbiaasia_doctor)


        
        if doc_form.is_valid() and image_form.is_valid():
            image_form.save()
            doc_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('/Doctor/update-profile')


    else:
         doc_form = DocProfileUpdateForm(instance=request.user.columbiaasia_doctor)
         image_form = DocImageForm(instance=request.user.columbiaasia_doctor)


    context = {

        'doc_form': doc_form,
        'image_form': image_form
    }

    return render(request, 'Update-DocProfile.html', context)