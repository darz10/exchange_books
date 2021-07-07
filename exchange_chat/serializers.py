from rest_framework import serializers
from login.models import Profile

from .models import Room, Exchange_chat


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = Profile
        fields = ["id", "username"]


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат обмена"""
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ["id", "creater", "invited", "date"]


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()
    class Meta:
        model = Exchange_chat
        fields = ["user", "text", "date"]


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Exchange_chat
        fields = ["room", "text"]