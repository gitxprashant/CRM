from contextlib import ContextDecorator
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    is_active=models.BooleanField('is_active',default=True)
    is_staff=models.BooleanField('is_staff',default=True)
    number= models.CharField(max_length=20)

    last_logout = models.DateTimeField(blank=True, null=True, verbose_name='last logout')











