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