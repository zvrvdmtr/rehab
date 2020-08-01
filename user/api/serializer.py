from rest_framework import serializers
from user.models import CustomUser
from djoser.serializers import UserCreateSerializer, UserSerializer


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'is_active', 'date_joined', 'email', 'date_of_birth', 'password')


class CustomUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'is_active', 'date_joined', 'email', 'date_of_birth')
