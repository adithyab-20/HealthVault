from django.db import models

class Doctor_Info(models.Model):

    REQUIRED_FIELDS = ['full_Name','Doctor_ID','Specialization','Education']

    full_Name = models.CharField(max_length=100)
    Doctor_ID = models.IntegerField()
    Specialization = models.TextField()
    Education = models.TextField()
    Overview = models.TextField()
    Work_Experience = models.TextField()

    def __str__(self):
        return self.Full_name

