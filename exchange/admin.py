from django.contrib import admin
from .models import Author, Book, Comment, Genre, Image_book, Rating


admin.site.register(Book)
admin.site.register(Image_book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)
