from rest_framework import serializers
from users.models import CustomUser
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)
    website = serializers.CharField(required=False, validators=[URLValidator()])

    def validate_website(self, value):
        validator = URLValidator()
        try:
            validator(value)
        except ValidationError:
            raise serializers.ValidationError("Некорректный URL-адрес")
        return value
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password', 'role', 'date_of_birth', 'company_name', 'address_company', 'license_number', 'website']

    def validate(self, data):
        data = super().validate(data)
        # Проверка на соответствие паролей
        if 'password' not in data or 'confirm_password' not in data:
            raise ValidationError("Оба поля 'password' и 'confirm_password' обязательны.")
        
        if data['password'] != data['confirm_password']:
            raise ValidationError("Пароли не совпадают!")

        # Проверка уникальности email
        if CustomUser.objects.filter(email=data['email']).exists():
            raise ValidationError("Пользователь с таким email уже существует!")

        # Проверка уникальности phone_number
        if CustomUser.objects.filter(phone_number=data['phone_number']).exists():
            raise ValidationError("Пользователь с таким номером телефона уже существует!")
        
        # Валидация обязательных полей в зависимости от роли
        role = data.get('role')

        if role == 'client':
            if not data.get('phone_number'):
                raise ValidationError({"phone_number": "Номер телефона обязательна для клиентов."})
            if not data.get('email'):
                raise ValidationError({"email": "Электронная почта обязательна для клиентов."})

        elif role == 'realtor':
            if not data.get('phone_number'):
                raise ValidationError({"phone_number": "Номер телефона обязательна для риелторов."})
            if not data.get('email'):
                raise ValidationError({"email": "Электронная почта обязательна для риелторов."})
            if not data.get('company_name'):
                raise ValidationError({"company_name": "Название компании обязательно для риэлторов."})

        elif role == 'developer':
            if not data.get('company_name'):
                raise ValidationError({"company_name": "Название компании обязательно для застройщиков."})
            if not data.get('address_company'):
                raise ValidationError({"address_company": "Адрес компании обязателен для застройщиков."})
            if not data.get('phone_number'):
                raise ValidationError({"phone_number": "Номер телефона обязательна для застройщиков."})
            if not data.get('email'):
                raise ValidationError({"email": "Электронная почта обязательна для застройщиков."})
            if not data.get('website'):
                raise ValidationError({"website": "Веб-сайт обязателен для застройщиков."})

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(**validated_data)

