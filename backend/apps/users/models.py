from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    USER_TYPES = [
        ('client', 'Клиент'),
        ('realtor', 'Риелтор'),
        ('developer', 'Застройщик'),
    ]

    # Основные поля
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        blank=True
    )  # Рейтинг только для риелторов
    is_verified = models.BooleanField(default=False)  # Статус верификации

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})"