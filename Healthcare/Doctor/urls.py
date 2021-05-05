from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "Doctor"

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name='Doctor_login.html'), name='Login'),
    path("Diagnosis", views.Latest_Diagnosis, name="LatestDiagnosisForm"),
]