from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    role_choice = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Moderator', 'Moderator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userprofile")
    role = models.CharField(max_length=10, choices=role_choice, default='User')
