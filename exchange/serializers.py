from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import *
from login.models import Profile


class RatingSerializer(serializers.ModelSerializer):
    """Сериализация рейтинга книг"""
    class Meta:
        model = Rating
        fields = ['value']

        def create(self, validated_data):
            rating, _ = Rating.objects.update_or_create(
                ip=validated_data.get('ip', None),
                movie=validated_data.get('movie', None),
                defaults={'star': validated_data.get("star")}
            )
            return rating


class CreateCommentSerializer(serializers.ModelSerializer):
    """Создание сериализации коментариев"""
    username = SlugRelatedField(slug_field='username', queryset=Profile.objects.all())
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Вывод коментариев"""
    username = SlugRelatedField(slug_field='username', queryset=Profile.objects.all())
    class Meta:
        model = Comment
        exclude = ['id', 'book']


class PhotoBook(serializers.ModelSerializer):
    """Фото книги"""
    class Meta:
        model = Image_book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Сериализация списка книг"""
    user = SlugRelatedField(slug_field='username', queryset=Profile.objects.all())
    image_book = PhotoBook(many=True)
    genre = SlugRelatedField(slug_field='genre', queryset=Genre.objects.all())
    author = SlugRelatedField(slug_field='name_author', queryset=Author.objects.all())
    rate_book = RatingSerializer(many=True)
    comment_book = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ['user', 'name_book', 'author', 'genre', 'country', 'book_describe', 'image_book', 'book_state', 'exchange_status', 'rate_book', 'comment_book']


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = Profile
        exclude = ['password']

