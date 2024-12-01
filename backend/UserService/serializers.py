from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs.get('role') != 'user':
            raise serializers.ValidationError("Для этой роли используйте другой сериализатор.")
        if not attrs.get('email'):
            raise serializers.ValidationError("Email обязателен для пользователя.")
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        return user


class PartnerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'role', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def validate(self, attrs):
        if attrs.get('role') != 'partner':
            raise serializers.ValidationError("Для этой роли используйте другой сериализатор.")
        if not attrs.get('email') or not attrs.get('first_name') or not attrs.get('last_name'):
            raise serializers.ValidationError("Для партнеров обязательны email, имя и фамилия.")
        return attrs

    def create(self, validated_data):

        partner = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            role=validated_data['role'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return partner