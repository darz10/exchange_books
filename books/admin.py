from django.contrib import admin
from .models import Author, Book, Category, Comment, Genre, Image_book, Rating


admin.site.register(Book)
admin.site.register(Image_book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)
