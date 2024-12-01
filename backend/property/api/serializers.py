from rest_framework import serializers
from property.models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',  # ID объекта
            'address',  # Адрес объекта
            'city',  # Город
            'state',  # Регион
            'country',  # Страна
            'postal_code',  # Почтовый индекс
            'property_type',  # Тип недвижимости
            'layout',  # Планировка
            'price',  # Цена
            'status',  # Статус
            'bedrooms',  # Количество спален
            'bathrooms',  # Количество ванных комнат
            'area',  # Площадь
            'description',  # Описание объекта
            'amenities',  # Удобства
            'year_built',  # Год постройки
            'developer',  # Застройщик
            'media',  # Основное изображение или документ
            'floor_plan',  # План этажей
            'agent_name',  # Имя риелтора/агента
            'agent_phone',  # Контактный телефон агента
            'agent_email',  # Контактный email агента
            'created_at',  # Дата создания
            'updated_at',  # Дата последнего обновления
        ]
