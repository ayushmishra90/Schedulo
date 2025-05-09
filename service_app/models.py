from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(default=60,max_digits=10, decimal_places=2)
    duration = models.IntegerField(default=60, help_text="Duration in minutes")  # Default value set to 60
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField(default=timezone.now) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.customer.username} - {self.service.name} - {self.status}  on {self.date}"
    def can_change_status(self, user):
        """Check if the user is the owner of the service"""
        return self.service.owner == user