from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('partner', 'Partner'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_partner(self):
        return self.role == 'partner'
    
    def is_user(self):
        return self.role == 'user'