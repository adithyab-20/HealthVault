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
    

# @json_view
# def Signup(request):
#     form = SignupForm(request.POST or None)
#     context = {}
#     if form.is_valid():
#         form.save()
#         Patient_fullname = form.cleaned_data.get('full_name')
#         Patient_email = form.cleaned_data.get('email')
#         raw_password = form.cleaned_data.get('password1')
#         account = authenticate(email=Patient_email, password=raw_password)
#         login(request,account)
#         return {'success' : True }


#     ser_instance = serializers.serialize('json', [ instance, ])
    
#     context.update(csrf(request))

#     form_html = render(request, 'Patient_Signup.html', context)
    
#     return {'success': False, 'form_html': form_html}


def Signup(request):
    if request.method == 'POST':
        resp = {}
        form = SignupForm(data=request.POST)
        if form.is_valid():
            resp['success'] = True
            print("Form Valid!")
            form.save()
            Patient_fullname = form.cleaned_data.get('full_name')
            Patient_email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=Patient_email, password=raw_password)
            login(request,account)
            print("Sucess!")
            

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

    return render(request, 'signupform.html', {'form': form})

