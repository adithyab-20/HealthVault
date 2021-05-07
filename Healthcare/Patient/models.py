from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from PIL import Image

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


class Patient_medical_history(models.Model):

    REQUIRED_FIELDS = ['Full_name','Age','Gender','Blood_Group']
    
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    Age = models.IntegerField(default=0)
    Gender = models.CharField(max_length=20, default="Null")
    Height = models.IntegerField(default=0)
    Weight = models.IntegerField(default=0)
    Blood_Group =  models.CharField(max_length=5, default="Null")
    Alchohol_Consumption = models.TextField(default="Null")
    Smoking_Habit = models.TextField(default="Null")
    Drug_Allergies = models.TextField(default="Null")
    Current_Medications = models.TextField(default="Null")

    def __str__(self):
        return f'{self.user.full_name} Medical History'


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.full_name} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height >300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)