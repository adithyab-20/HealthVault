from django.urls import path
from . import views


app_name = "Patient"

urlpatterns = [
    path("", views.loginView,name='login'),

]