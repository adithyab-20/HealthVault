from django.urls import path
from . import views


app_name = "Patient"

urlpatterns = [
    path("", views.loginView,name='login'),
    path("medical", views.medformview, name="MedHistoryForm"),
    path("success", views.success, name="Success"),
    path("dashboard", views.dashboard, name="Dashboard"),
    path("select-doctor", views.docselection, name="Docselection")
]