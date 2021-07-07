# Generated by Django 3.2.4 on 2021-07-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210707_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag',
            new_name='name_hashtag',
        ),
        migrations.AlterField(
            model_name='book',
            name='hashtag',
            field=models.ManyToManyField(blank=True, related_name='hashtag', to='books.Hashtag'),
        ),
    ]
