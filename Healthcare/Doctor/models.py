from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from Patient.models import Account
from PIL import Image

# Create your models here.


class ColumbiaAsia_Doctor(models.Model):
    
    doctor = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    id_doctor               = models.IntegerField(unique=True)
    image                   = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department              = models.CharField(max_length=100)
    education               = models.CharField(max_length=200)
    specialization          = models.CharField(max_length=100)
    work_experience         = models.TextField()
    doc_overview            = models.TextField()

    def __str__(self):
        return f'{self.doctor.full_name} Profile'

    def save(self, *args, **kwargs):
            super(ColumbiaAsia_Doctor, self).save(*args, **kwargs)

            img = Image.open(self.image.path)
            
            if img.height >300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)




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
