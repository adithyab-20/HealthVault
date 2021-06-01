from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Doctor.models import Doctor_latest_diagnosis,Doctor_CA

# Register your models here.

class ColumbiaAsiaAdminArea(admin.AdminSite):
    site_header = "ColumbiaAsia Admin"


columbia_asia = ColumbiaAsiaAdminArea(name='ColumbiaAsia')

columbia_asia.register(Doctor_CA)

class ApolloAdminArea(admin.AdminSite):
    site_header = "Apollo Hospital Admin"

apollo = ApolloAdminArea(name="Apollo")

columbia_asia.register(Doctor_latest_diagnosis)