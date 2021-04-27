from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Patient_medical_history

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


admin.site.register(Patient_medical_history)