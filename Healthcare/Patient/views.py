from django.shortcuts import render
from django.contrib.auth import login, authenticate
from Patient.forms import SignupForm
from django.contrib import messages
from jsonview.decorators import json_view
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from Patient.forms import MedicalHistoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from Patient.decorators import *

# def Signup(request):
#     context = {}
#     if request.method == 'POST':
#         form = SignupForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             Patient_fullname = form.cleaned_data.get('full_name')
#             Patient_email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=Patient_email, password=raw_password)
#             login(request,account)
#             messages.success(request, f'Account created for {Patient_fullname}!')

#         else:
#             context['form'] = form
#             print(form.errors)
#     else:
#         form = SignupForm()
#         context['form'] = form
#     return render(request, 'signupform.html', context)

# def Login(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             P_username = form.cleaned_data.get('P_username')
#     else:
#         form = UserCreationForm()
#     return render(request, 'Patient_Signup.html', {'form': form})
    
@unauthenticated_user
def loginView(request):

    context = {}

    if request.method == 'POST':
        signin_form = AuthenticationForm(data=request.POST)
        if signin_form.is_valid():
            user = signin_form.get_user()
            login(request, user)
            return redirect('/Patient/dashboard')
        else:
            context['signin_form'] = signin_form
            context['signin_form_errors'] = signin_form.errors
            print(context['signin_form_errors'])
    else:
        signin_form = AuthenticationForm()
        context['signin_form'] = signin_form

    if request.method == 'POST' and request.is_ajax():
        resp = {}
        form = SignupForm(data=request.POST)
        if form.is_valid():
            resp['success'] = True
            user = form.save()
            Patient_fullname = form.cleaned_data.get('full_name')
            Patient_email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            group = Group.objects.get(name='Patients')
            user.groups.add(group)

            account = authenticate(email=Patient_email, password=raw_password)
            login(request,account)
            
        else:
            resp['success'] = False
            print(form.errors)
            csrf_context = {}
            csrf_context.update(csrf(request))
            signup_form_html = render_crispy_form(form, context=csrf_context)
            resp['html'] = signup_form_html
            print(resp)
        return HttpResponse(json.dumps(resp), content_type='application/json')

    
    form = SignupForm()
    context['form'] = form
    return render(request, 'signupform.html', context)

@login_required()
def medformview(request):
    context = {}
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_Fullname = form.cleaned_data.get('Full_name')
            # Patient_DateofBirth = form.cleaned_data.get('DOB')
            Patient_age = form.cleaned_data.get('Age')
            Patient_gender = form.cleaned_data.get('Gender')
            Patient_height = form.cleaned_data.get('Height')
            Patient_weight = form.cleaned_data.get('Weight')
            Patient_bloodgroup = form.cleaned_data.get('Blood_Group')
            Patient_alchohol = form.cleaned_data.get('Alchohol_Consumption')
            Patient_smoking = form.cleaned_data.get('Smoking_Habit')
            Patient_drugallergies = form.cleaned_data.get('Drug_Allergies')
            Patient_medications = form.cleaned_data.get('Current_Medications')
            return redirect('/Patient/dashboard')

        else:
            context['form'] = form
            print(form.errors)
    else:
        form = MedicalHistoryForm()
        context['form'] = form
    return render(request, 'Medical_History_form.html', context)



def success(request):
    return render(request, 'Success.html')

@login_required(login_url="{% url 'Patient:login' %}")
@allowed_users(allowed_roles=['Admin', 'Patients'])
def dashboard(request):
    return render(request, 'new-dash.html')

@login_required()
def docselection(request):
    return render(request, 'doctor-Selection.html')



def doctor_redirect(request):
    return render(request, 'Doctor-Redirect.html')