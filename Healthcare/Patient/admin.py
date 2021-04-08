from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

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
admin.site.register(Account, AccountAdminConfig)

class MedicalHistoryConfig(UserAdmin):
    search_fields = ('Full_name','Age')
    list_display = ('Full_name','DOB','Age','Gender','Height','Weight','Blood_Group','Alchohol_Consumption','Smoking_Habit','Drug_Allergies','Current_Medications',)
    list_filter = ('Full_name','Blood_Group','Gender')
    ordering = ('Full_name',)
    readonly_fields = ('Height','Weight')

    fieldsets = (
        (None, {'fields': ('DOB','Blood_Group')}),
        ('Personal', {'fields': ('Full_name',)}),

    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
        'fields': ('Full_name','DOB','Age','Gender','Blood_Group','Weight')
        }),
    )
admin.site.register(Patient_medical_history, MedicalHistoryConfig)
