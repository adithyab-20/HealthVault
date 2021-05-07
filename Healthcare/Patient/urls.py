from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "Patient"

urlpatterns = [
    path("", views.loginView,name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("medical", views.medformview, name="MedHistoryForm"),
    path("success", views.success, name="Success"),
    path("dashboard", views.dashboard, name="Dashboard"),
    path("select-doctor", views.docselection, name="Docselection"),
    path("doctor-redirect", views.doctor_redirect, name="DocRedirect"),
    path("update-profile", views.profile, name="Profile")
]