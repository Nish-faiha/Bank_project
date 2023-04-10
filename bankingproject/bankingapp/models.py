from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomerModel(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.BooleanField()
    phonenumber=models.CharField(max_length=250)
    email=models.EmailField()
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    accounttype=models.CharField(max_length=250)
    materialsprovide=models.CharField(max_length=250)

    def __str__(self):
            return self.name


