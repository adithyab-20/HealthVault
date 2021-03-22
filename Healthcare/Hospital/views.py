from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            H_username = form.cleaned_data.get('H_username')
    else:
        form = UserCreationForm()
    return render(request, 'Hospital_login.html', {'form': form})