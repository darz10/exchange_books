# Generated by Django 3.2.4 on 2021-06-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_auto_20210622_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='url',
        ),
    ]