from django.db.models import fields
from rest_framework import serializers
from .models import Profile
from books.serializers import BookSerializer


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей и их книги"""

    owner = BookSerializer(many=True)
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'avatar', 'age', 'owner']