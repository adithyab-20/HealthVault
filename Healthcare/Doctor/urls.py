from django.urls import path
from . import views

urlpatterns = [
    path("", views.Login, name="Login"),
    path("Diagnosis", views.Latest_Diagnosis, name="LatestDiagnosisForm"),
]