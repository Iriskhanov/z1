from django.db import models

class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('under_construction', 'Under Construction'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
    ]

    address = models.CharField(max_length=255)  # Адрес объекта
    city = models.CharField(max_length=100)  # Город
    state = models.CharField(max_length=100, null=True, blank=True)  # Регион
    country = models.CharField(max_length=100, null=True, blank=True)  # Страна
    postal_code = models.CharField(max_length=20, null=True, blank=True)  # Почтовый индекс

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='apartment')  # Тип недвижимости
    layout = models.JSONField(null=True, blank=True)  # Планировка (JSON для гибкости)
    price = models.DecimalField(max_digits=15, decimal_places=2)  # Цена
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')  # Статус

    bedrooms = models.PositiveIntegerField(default=1)  # Количество спален
    bathrooms = models.PositiveIntegerField(default=1)  # Количество ванных комнат
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in square meters")  # Площадь

    description = models.TextField(null=True, blank=True)  # Описание объекта
    amenities = models.JSONField(null=True, blank=True, help_text="List of amenities in JSON format")  # Удобства

    year_built = models.PositiveIntegerField(null=True, blank=True)  # Год постройки
    developer = models.CharField(max_length=255, null=True, blank=True)  # Застройщик

    media = models.FileField(upload_to='properties/', null=True, blank=True)  # Медиа (изображения или документы)
    floor_plan = models.FileField(upload_to='floor_plans/', null=True, blank=True)  # План этажей

    agent_name = models.CharField(max_length=255, null=True, blank=True)  # Имя риелтора/агента
    agent_phone = models.CharField(max_length=20, null=True, blank=True)  # Контактный телефон агента
    agent_email = models.EmailField(null=True, blank=True)  # Контактный email агента

    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления

    def __str__(self):
        return f"{self.property_type.capitalize()} at {self.address}"
