from django.urls import path
from . import views


app_name = "Hospital"

urlpatterns = [
    path("", views.Login, name="Login"),
    path("submit", views.test, name="test")
]