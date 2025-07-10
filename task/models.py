from django.db import models
import time
# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=150)
    priority = models.CharField(max_length=150)
    date = models.DateField()
    task_complete = models.BooleanField(default=False)

class Account(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)