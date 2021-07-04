from django.db import models
from login.models import Profile


class Room(models.Model):
    """Модель комнаты чата"""
    creater = models.ForeignKey(Profile, verbose_name="Создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(Profile, verbose_name="Участник", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Exchange_chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Room, verbose_name="Комната обмена", on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"