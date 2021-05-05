from django.contrib import admin
from . import models 
from Patient import models as Pmodels

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ColumbiaAsiaAdminArea(admin.AdminSite):
    site_header = "ColumbiaAsia Admin"


columbia_asia = ColumbiaAsiaAdminArea(name='ColumbiaAsia')

columbia_asia.register(models.ColumbiaAsia_Doctor)





class AccountAdminConfig(UserAdmin):
    search_fields = ('email', 'full_name')
    list_display = ('email','full_name', 'date_joined', 'last_login', 'is_admin', 'is_staff',)
    list_filter = ('email', 'is_active', 'is_staff')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email','password')}),
         ('Personal', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
       
    )
    
    add_fieldsets = (
        (None, {'classes': ('wide',),
        'fields': ('email', 'full_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin')
        }),
    )

columbia_asia.register(Pmodels.Account, AccountAdminConfig)

class ApolloAdminArea(admin.AdminSite):
    site_header = "Apollo Hospital Admin"

apollo = ApolloAdminArea(name="Apollo")