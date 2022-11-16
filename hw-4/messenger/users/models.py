from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=32, unique=True)
#     email = models.CharField(max_length=256, unique=True)
#     password = models.CharField(max_length=50)
#     registered_at = models.DateTimeField(auto_now_add=True)
#     bio = models.CharField(max_length=70, blank=True)


class User(AbstractUser):
    bio = models.CharField(max_length=70, blank=True, verbose_name='Биография')
    phone_number = models.CharField(max_length=50, blank=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
