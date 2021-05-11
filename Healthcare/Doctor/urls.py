from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "Doctor"

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name='Doctor_login.html'), name='Login'),
    path("logout", auth_views.LogoutView.as_view(template_name="Doc_Logout.html"), name='Logout'),
    path("Diagnosis", views.Latest_Diagnosis, name="LatestDiagnosisForm"),
    path("dashboard", views.dashboard, name="Dashboard"),
    path("patient-redirect", views.patient_redirect, name="PatientRedirect"),
    path("update-profile", views.profile, name="Profile"),
    path("patient-requests", views.request_view, name="PatientRequests")
]