from django.shortcuts import render
from django.contrib.auth import login, authenticate
from Patient.forms import SignupForm, MedicalHistoryForm, ProfileUpdateForm
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from Patient.decorators import *
from Patient.models import Account,Profile
from Doctor.models import ColumbiaAsia_Doctor

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
            
            Profile.objects.create(user=request.user)
            
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
            pat = form.save(commit=False)
            pat.user = request.user
            pat.save()
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

    context = {}

    context['neurology'] = ColumbiaAsia_Doctor.objects.filter(department="Neurology")
    context['oncology'] = ColumbiaAsia_Doctor.objects.filter(department="Oncology")
    context['cardiology'] = ColumbiaAsia_Doctor.objects.filter(department="Cardiology")
    context['diagmed'] = ColumbiaAsia_Doctor.objects.filter(department="Diagnostic_Medicine")

    return render(request, 'doctor-Selection.html', context)



def doctor_redirect(request):
    return render(request, 'Doctor-Redirect.html')

@login_required()
def profile(request):
    if request.method == 'POST':
        medupdate_form = MedicalHistoryForm(request.POST, instance=request.user.patient_medical_history)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)

        
        if medupdate_form.is_valid() and p_form.is_valid():
            medupdate_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('/Patient/update-profile')



    
    else:
         medupdate_form = MedicalHistoryForm(instance=request.user.patient_medical_history)
         p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        
        'medupdate_form': medupdate_form,
        'p_form': p_form
    }

    return render(request, 'Update-Profile.html', context)


   


def send_doctor_request(request, *args, **kwargs):
	user = request.user
	payload = {}
	if request.method == "POST" and user.is_authenticated:
		user_id = request.POST.get("receiver_user_id")
		if user_id:
			receiver = Account.objects.get(pk=user_id)
			try:
				# Get any friend requests (active and not-active)
				friend_requests = FriendRequest.objects.filter(sender=user, receiver=receiver)
				# find if any of them are active (pending)
				try:
					for request in friend_requests:
						if request.is_active:
							raise Exception("You already sent them a friend request.")
					# If none are active create a new friend request
					friend_request = FriendRequest(sender=user, receiver=receiver)
					friend_request.save()
					payload['response'] = "Friend request sent."
				except Exception as e:
					payload['response'] = str(e)
			except FriendRequest.DoesNotExist:
				# There are no friend requests so create one.
				friend_request = FriendRequest(sender=user, receiver=receiver)
				friend_request.save()
				payload['response'] = "Friend request sent."

			if payload['response'] == None:
				payload['response'] = "Something went wrong."
		else:
			payload['response'] = "Unable to sent a friend request."
	else:
		payload['response'] = "You must be authenticated to send a friend request."
	return HttpResponse(json.dumps(payload), content_type="application/json")
