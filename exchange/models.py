from django.db import models
from login.models import Profile


STATE = (
	('Отличное', 'Отличное'),
	('Хорошее', 'Хорошее'),
	('Среднее', 'Среднее'),
	('Плохое', 'Плохое')
)


class Book(models.Model):
    """Книги"""

    user = models.ForeignKey(Profile, 
                            on_delete=models.CASCADE, 
                            verbose_name='Владелец книги', 
                            related_name='owner')
    name_book = models.CharField(verbose_name='Название книги', 
                                max_length=70)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    country = models.CharField(verbose_name='Страна', max_length=50)
    book_describe = models.TextField(verbose_name='Описание книги', max_length=300)
    book_state = models.CharField(verbose_name='Состояние книги', 
                                max_length=50,choices=STATE, 
                                default='хорошее')
    exchange_status = models.BooleanField(verbose_name='Статус готовности обмена книги', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.name_book} - {self.author}"


class Image_book(models.Model):
    """Изображение книги"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="image_book", verbose_name='Книга')
    image_book = models.ImageField(upload_to='image_book', 
                                    verbose_name='Изображение книги',
                                    blank=True,
                                    null=True)

    def __str__(self):
        return f'{self.image_book} - {self.book}'

   
class Author(models.Model):
    """Авторы"""

    name_author = models.CharField(verbose_name='Имя автора', max_length=70)
    describe_author = models.TextField(verbose_name='Описание автора',max_length=300)
    photo_author = models.ImageField(upload_to='photo_author', verbose_name='Фото автора')
    
    def __str__(self):
        return self.name_author


class Category(models.Model):
    """Категории"""

    category = models.CharField(verbose_name="Категория", max_length=150)
    

class Genre(models.Model):
    """Жанры"""

    genre = models.CharField(verbose_name='Жанр', max_length=50)

    def __str__(self):
        return self.genre


class Rating(models.Model):
    """Рейтинг книги"""

    value = models.SmallIntegerField("Значение", default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='rate_book')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        ordering = ["-value"]

    
class Comment(models.Model):
    """Коментарии"""
    
    book = models.ForeignKey(Book, 
                            on_delete=models.CASCADE, 
                            verbose_name='Книга', 
                            related_name='comment_book')
    username = models.ForeignKey(Profile, 
                                on_delete=models.CASCADE, 
                                related_name="children", 
                                verbose_name='Пользователь')
    comment_name = models.CharField(verbose_name='Название коментария', max_length=200)
    comment_text = models.TextField(verbose_name='Текст коментария', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Когда создан коментарий')

    def __str__(self):
        return f"{self.comment_name} - {self.book} - {self.username}"