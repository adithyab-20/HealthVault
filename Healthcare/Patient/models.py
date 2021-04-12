from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    