from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


#WHEN WE CREATE NEW USER WE MUST GENERATE A REQUEST LIST
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields): 
        
        if not email:
            raise ValueError("Users must have an email Address!")

        email = self.normalize_email(email)
        user = self.model(
            email = email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser must be assigned to is_staff=True"
            )
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True"
            )

        if other_fields.get('is_admin') is not True:
            raise ValueError(
                "Superuser must be assigned to admin=True"
            )
        user = self.create_user(
            email, password, **other_fields,
        )

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    full_name               = models.CharField(max_length=60)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = MyAccountManager() 

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


# class Patient_medical_history(models.Model):

#     REQUIRED_FIELDS = ['Full_name','Age','Gender','Blood_Group']
#     Full_name = models.CharField(max_length=100)
#     Age = models.IntegerField()
#     Gender = models.CharField(max_length=20)
#     Contact_Number = models.IntegerField()
#     Height = models.IntegerField()
#     Weight = models.IntegerField()
#     Blood_Group =  models.CharField(max_length=5)
#     Previous_Illness = models.TextField()
#     Alchohol_Consumption = models.TextField()
#     Smoking_Habit = models.TextField()
#     Drug_Allergies = models.TextField()
#     Current_Medications = models.TextField()

#     def __str__(self):
#         return self.Full_name


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.full_name} Profile'

class Patient_List(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    doctors = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name="doctors")

    def __str__(self):
        return self.user.full_name

    #This is if patient can have multiple doctors in doctor list
    #def add_doctor(self, account):
        #if not account in self.doctors.all():
            #self.doctors.add(account)
            #self.save()

    def remove_doctor(self,account):
        #   Remove a doctor or unenroll from doctor
        if account in self.doctors.all():
            self.doctors.remove(account)


class Doctor_Request(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor")
    #we are gonna define a field is_active to see if request is active or not
    #doctor request becomes inactive if it gets accepted
    Is_Active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.full_name

    def accept(self):
        #accept a patient's request
        doctor_request_list = Patient_List.objects.get(user=self.doctor)
        if doctor_request_list:
            doctor_request_list.add_patient(self.patient)
            self.Is_Active = False
            self.save()

    def decline(self):
        #It is declined by setting is_active field to False
        self.Is_Active = False
        self.save()

    def cancel(self):
        #Cancel a doctor request
        #It is cancelled by setting is_active field to False
        self.Is_Active = False
        self.save()
     