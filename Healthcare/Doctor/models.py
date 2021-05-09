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

    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    patient_ID = models.IntegerField()
    doctor_ID = models.IntegerField()
    department = models.CharField(max_length=100)
    date_of_updation =  models.DateField()
    diagnosis = models.TextField()
    diagnosis_description = models.TextField()
    doctor_advice = models.TextField()
    additional_comments = models.TextField()

    def __str__(self):
        return self.Patient_name
