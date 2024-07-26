from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, default='user')

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email'] 
    #has no effect in admin ui, it is list of the field names that will be prompted for when creating a user via the createsuperuser