from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def homeview(request):
    return render(request, 'HomePageFinal.html')