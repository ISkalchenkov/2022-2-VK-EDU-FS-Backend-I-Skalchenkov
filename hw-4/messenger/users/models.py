from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=70, blank=True, verbose_name='Биография')
    phone_number = models.CharField(max_length=50, blank=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
