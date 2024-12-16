from rest_framework import serializers
from django.contrib.auth import get_user_model 
from join_auth.models import UserProfile


CustomUser = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    selected = serializers.BooleanField(write_only=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'fullname', 'initials', 'initialsColor', 'phone', 'email', 'selected']
        read_only_fields = ['id', 'initials', 'initialsColor']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if 'email' in validated_data and instance.user.email != validated_data['email']:
            instance.user.email = validated_data['email']
            instance.user.save()
        instance.save()
        return instance


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already taken.')
        return value

    def validate_username(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError("The username must contain exactly two words.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        profile = user.profile
        profile.phone = "123456704343" 
        profile.save()
        return user
