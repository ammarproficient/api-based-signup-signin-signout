from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_phone(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("Phone number must be 13 digits (e.g., 0123456789100)")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this phone number already exists")
        return value

    def validate(self, data):
        # Password match check
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")

        # Phone number duplication check
        if User.objects.filter(username=data['phone']).exists():
            raise serializers.ValidationError({"phone": "A user with this phone number already exists"})

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['phone'],
            first_name=validated_data['name'],
            password=make_password(validated_data['password'])
        )
        return user
