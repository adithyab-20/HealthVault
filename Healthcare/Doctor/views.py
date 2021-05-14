from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Doctor.decorators import *
from Doctor.forms import DocProfileUpdateForm, DocImageForm
from django.contrib import messages
from Patient.models import Account
from Doctor.models import Patient_List, Doctor_Request, Doctor_Assigned_To_Patient, ColumbiaAsia_Doctor
from Doctor.doctor_request_status import DoctorRequestStatus
from Doctor.utils import get_doctor_request_or_false

def request_view(request, *args, **kwargs):
	context = {}
	user_id = request.user.id
	print(user_id)
	try:
		account = Account.objects.get(pk=user_id)
	except:
		return HttpResponse("Something went wrong.")
	
	if account:
		context['id'] = account.id
		context['full_name'] = account.full_name
		context['email'] = account.email
		context['image'] = account.columbiaasia_doctor.image.url

		try:
			patient_list = Patient_List.objects.get(doctor=account)
		except Patient_List.DoesNotExist:
			patient_list = Patient_List(user=account)
			patient_list.save()
		patients = patient_list.patients.all()
		context['patients'] = patients

		request_sent = DoctorRequestStatus.NO_REQUEST_SENT.value
		patient_requests = get_doctor_request_or_false(doctor=account)
	
		if patient_requests!= False:
			request_sent = DoctorRequestStatus.THEM_SENT_TO_YOU.value
			context['patient_requests'] = patient_requests
		else:
			request_sent = DoctorRequestStatus.NO_REQUEST_SENT.value 

		# Set the template variables to the values
		context['request_sent'] = request_sent
		context['patient_requests'] = patient_requests
		return render(request, "Patient_Requests.html", context)	   


@login_required(login_url="/Doctor")
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