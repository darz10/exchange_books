# Generated by Django 3.2.4 on 2021-06-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-value']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='url',
        ),
        migrations.AlterField(
            model_name='author',
            name='describe_author',
            field=models.TextField(max_length=300, verbose_name='Описание автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name_author',
            field=models.CharField(max_length=70, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo_author',
            field=models.ImageField(upload_to='photo_author', verbose_name='Фото автора'),
        ),
    ]
