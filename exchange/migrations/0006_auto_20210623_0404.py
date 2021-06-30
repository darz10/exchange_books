# Generated by Django 3.2.4 on 2021-06-23 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0005_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец книги'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=200, verbose_name='Название коментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=4000, verbose_name='Текст коментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Когда создан коментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=50, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='image_book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.book', verbose_name='Книга'),
        ),
    ]