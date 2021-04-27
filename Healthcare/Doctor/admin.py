from django.contrib import admin
from . import models 

# Register your models here.

class ColumbiaAsiaAdminArea(admin.AdminSite):
    site_header = "ColumbiaAsia Admin"


columbia_asia = ColumbiaAsiaAdminArea(name='ColumbiaAsia')

columbia_asia.register(models.Doctor_CA)

class ApolloAdminArea(admin.AdminSite):
    site_header = "Apollo Hospital Admin"

apollo = ApolloAdminArea(name="Apollo")