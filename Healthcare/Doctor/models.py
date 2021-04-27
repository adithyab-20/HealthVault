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
