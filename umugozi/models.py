from django.db import models

# Create your models here.
class Person(models.Model):
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    username = models.CharField(max_length=10, default='user')
    email = models.CharField(max_length=80)
    dob= models.DateField()
    address= models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    password= models.CharField(max_length=30)


