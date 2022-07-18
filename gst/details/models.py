from django.db import models

# Create your models here.

class VikasCustomerDetail(models.Model):
    date=models.DateField(max_length=50)
    cx_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=40)
    disposition1=models.CharField(max_length=50)
    disposition2=models.CharField(max_length=50)

class TanyaCustomerDetail(models.Model):
    date=models.DateField(max_length=50)
    cx_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=40)
    disposition1=models.CharField(max_length=50)
    disposition2=models.CharField(max_length=50)

class AmanCustomerDetail(models.Model):
    date=models.DateField(max_length=50)
    cx_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=40)
    disposition1=models.CharField(max_length=50)
    disposition2=models.CharField(max_length=50)