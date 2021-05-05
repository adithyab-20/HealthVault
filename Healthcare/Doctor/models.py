from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from Patient.models import Account
# Create your models here.


# class Doctor_CA(models.Model):
    
#     full_name = models.CharField(max_length=100)
# #       full_name               = models.CharField(max_length=60)
#     doctor_id               = models.IntegerField( unique=True)
#     department              = models.CharField(max_length=100)
#     education               = models.CharField(max_length=200)
#     specialization          = models.CharField(max_length=100)
#     work_experience         = models.TextField()
#     doc_overview            = models.TextField()

#     def __str__(self):
#         return self.full_name

class ColumbiaAsia_Doctor(models.Model):
    
    doctor = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    id_doctor               = models.IntegerField(unique=True)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department              = models.CharField(max_length=100)
    education               = models.CharField(max_length=200)
    specialization          = models.CharField(max_length=100)
    work_experience         = models.TextField()
    doc_overview            = models.TextField()

    def __str__(self):
        return f'{self.doctor.full_name} Profile'

# class ColumbiaAsiaManager(BaseUserManager):
#     def create_user(self, email, password=None, **other_fields): 
        
#         if not email:
#             raise ValueError("Users must have an email Address!")

#         email = self.normalize_email(email)
#         user = self.model(
#             email = email, **other_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, **other_fields):
#         other_fields.setdefault('is_admin', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)
#         other_fields.setdefault('is_staff', True)
        
#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 "Superuser must be assigned to is_staff=True"
#             )
        
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 "Superuser must be assigned to is_superuser=True"
#             )

#         if other_fields.get('is_admin') is not True:
#             raise ValueError(
#                 "Superuser must be assigned to admin=True"
#             )
#         user = self.create_user(
#             email, password, **other_fields,
#         )

#         user.save(using=self._db)
#         return user


# class ColumbiaAsia_Doctor(User):

#     def __str__(self):
#         return self.username



class Doctor_latest_diagnosis(models.Model):

    REQUIRED_FIELDS = ['Full_name','Age','Gender','Blood Group']

    Patient_name = models.CharField(max_length=100)
    Doctor_name = models.CharField(max_length=100)
    Patient_ID = models.IntegerField()
    Doctor_ID = models.IntegerField()
    Department = models.CharField(max_length=100)
    Date_of_updation =  models.DateField()
    Diagnosis = models.TextField()
    Diagnosis_description = models.TextField()
    Doctor_advice = models.TextField()
    Additional_comments = models.TextField()

    def __str__(self):
        return self.Patient_name
