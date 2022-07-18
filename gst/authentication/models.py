from django.db import models

from django.contrib.auth.models import AbstractUser,AbstractBaseUser

class CustomUser(AbstractUser):
    is_staff= models.BooleanField('is_staff', default=False)
    is_active=models.BooleanField('is_active',default=True)
    last_logout = models.DateTimeField(blank=True, null=True, verbose_name='last logout')
    

class Staff(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)



class CustomerDetail(models.Model):
    date=models.DateField(max_length=50)
    cx_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=40)
    disposition1=models.CharField(max_length=50)
    disposition2=models.CharField(max_length=50)


def __str__(self):
    return self.user.username











