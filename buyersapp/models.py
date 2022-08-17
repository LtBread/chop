from django.db import models
from django.contrib.auth.models import AbstractUser


class Buyer(AbstractUser):
    avatar = models.ImageField(verbose_name='аватар', upload_to='buyers_avatars', blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def change_activity(self):
        self.is_active = not self.is_active
        self.save()
