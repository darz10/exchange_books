from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import *
from login.models import Profile


class HashtagSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Hashtag
        fields = ['name_hashtag']

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
        fields = ['image_book']


class BookSerializer(serializers.ModelSerializer):
    """Сериализация списка книг"""
    user = SlugRelatedField(slug_field='username', queryset=Profile.objects.all())
    image_book = PhotoBook(many=True)
    genre = SlugRelatedField(slug_field='genre', queryset=Genre.objects.all())
    author = SlugRelatedField(slug_field='name_author', queryset=Author.objects.all())
    rate_book = RatingSerializer(many=True)
    comment_book = CommentSerializer(many=True)
    hashtag = HashtagSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'user', 'name_book', 'author', 'genre', 'country', 'book_describe', 'image_book', 'book_state', 'exchange_status', 'hashtag', 'rate_book', 'comment_book']
