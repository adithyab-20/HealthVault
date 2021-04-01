from django.shortcuts import render
from django.contrib.auth import login, authenticate
from Patient.forms import SignupForm
from django.contrib import messages
from jsonview.decorators import json_view
from django.template.context_processors import csrf


# def Signup(request):
#     context = {}
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             Patient_fullname = form.cleaned_data.get('full_name')
#             Patient_email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=Patient_email, password=raw_password)
#             login(request,account)
#             messages.success(request, f'Account created for {Patient_fullname}!')

#         else:
#             context['signup_form'] = form
#     else:
#         form = SignupForm()
#         context['signup_form'] = form
#     return render(request, 'Patient_Signup.html', context)

def Login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            P_username = form.cleaned_data.get('P_username')
    else:
        form = UserCreationForm()
    return render(request, 'Patient_Signup.html', {'form': form})


@json_view
def Signup(request):
    form = SignupForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
        Patient_fullname = form.cleaned_data.get('full_name')
        Patient_email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        account = authenticate(email=Patient_email, password=raw_password)
        login(request,account)
        return {'success' : True }

    context.update(csrf(request))

    form_html = render(request, 'Patient_Signup.html', context)
    
    return {'success': False, 'form_html': form_html}