from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Buyer(AbstractUser):
    avatar = models.ImageField(verbose_name='аватар', upload_to='buyers_avatars', blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
