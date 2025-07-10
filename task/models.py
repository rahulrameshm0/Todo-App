from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=150)
    priority = models.CharField(max_length=150)
    date = models.DateField()
    task_complete = models.BooleanField(default=False)

class Account(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)