from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')
