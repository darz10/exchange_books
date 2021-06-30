from django.db import models

class Region(models.Model):
    """Модель региона"""
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        verbose_name = "Штат"
        verbose_name_plural = "Штаты"

    def __str__(self):
        return "{}".format(self.name)


class City(models.Model):
    """Модель города"""
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return "{}".format(self.name)
