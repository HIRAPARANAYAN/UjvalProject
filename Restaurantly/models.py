from django.db import models

# Create your models here.

class Bookatable(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    people = models.IntegerField()
    message = models.CharField(max_length=255)

class Contect(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)