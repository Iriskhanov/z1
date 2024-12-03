from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('realtor', 'Realtor'),
        ('developer', 'Developer')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    company_name = models.CharField(max_length=50, blank=True, null=True)
    address_company = models.TextField(blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    
    website = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(('email address'), unique = True)
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.username} - {self.get_role_display()}"
    
    