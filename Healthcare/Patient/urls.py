from django.urls import path
from . import views

app_name = "Patient"

urlpatterns = [
    path("", views.Signup, name="Signup"),
    path("", views.Login, name="Login"),
]