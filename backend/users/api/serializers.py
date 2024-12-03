from rest_framework import serializers
from users.models import CustomUser
from django.core.exceptions import ValidationError


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password', 'role', 'date_of_birth', 'company_name', 'address_company', 'license_number', 'website']

    def validate(self, data):
        # Проверка на соответствие паролей
        if data['password'] != data['confirm_password']:
            raise ValidationError("Пароли не совпадают!")

        # Проверка уникальности email
        if CustomUser.objects.filter(email=data['email']).exists():
            raise ValidationError("Пользователь с таким email уже существует!")

        # Проверка уникальности phone_number
        if CustomUser.objects.filter(phone_number=data['phone_number']).exists():
            raise ValidationError("Пользователь с таким номером телефона уже существует!")


        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'client'),
            date_of_birth=validated_data.get('date_of_birth', None),
            company_name=validated_data.get('company_name', ''),
            address_company=validated_data.get('address_company', ''),
            license_number=validated_data.get('license_number', ''),
            website=validated_data.get('website', ''),
        )
        return user
