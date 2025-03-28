from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class City(models.Model):  # Должна быть объявлена перед User, если используется в ForeignKey
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # Уберите упоминания favorite_pokemon_type, если его нет в модели
    # или добавьте поле в модель, если оно должно быть:
    # favorite_pokemon_type = models.ManyToManyField('PokemonType', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='pokemon_users',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='pokemon_users',
        blank=True,
    )



class Application(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('submitted', 'На рассмотрении'),
        ('approved', 'Одобрено'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)