from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Branch(models.Model):
    branch = models.CharField(max_length=100)
    branchid = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch

class Form(models.Model):
    name = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    age = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    gender = models.CharField( max_length=50,default='abc')
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone = models.CharField( max_length=50)
    account = models.CharField( max_length=50)
    
    