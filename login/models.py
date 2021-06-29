from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER = (
	('Мужской', 'Мужской'),
	('Женский', 'Женский')
)


class Profile(AbstractUser):
    """Кастомная модель пользователя"""
    gender = models.CharField(verbose_name='Пол', max_length=50,choices=GENDER, default='Мужской')
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True, verbose_name="Фото пользователя")
    age = models.PositiveIntegerField(verbose_name="Возраст", default=0) # check adult or not for filter content
    # address = models.CharField(verbose_name="Адрес", max_length=250)
    # postcode = models.CharField(verbose_name="Индекс", max_length=120)
    # phone = models.IntegerField(verbose_name="Телефон", default=790000000)
    # // TODO create separate app for country, state and sity(store)


    def __str__(self):
        return self.username

