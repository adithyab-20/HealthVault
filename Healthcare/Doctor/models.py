from django.db import models

# Create your models here.
class Doctor_CA(models.Model):
    
    full_name = models.CharField(max_length=100)
    doctor_id = models.IntegerField( unique=True)
    department = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    work_experience = models.TextField()
    doc_overview = models.TextField()

    def __str__(self):
        return self.full_name

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
