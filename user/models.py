from django.db import models
from django.contrib.auth.models import AbstractUser
from user.utils import CustomUserManager
import datetime

# Create your models here.


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
