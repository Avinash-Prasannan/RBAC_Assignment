from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data.get('username'),
            password=user_data.get('password'),
            email=user_data.get('email')
        )

        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile
