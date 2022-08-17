from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name='категории', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    name = models.CharField(verbose_name='имя продукта', max_length=256)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def __str__(self):
        return f'{self.name} | {self.category}'

    def change_activity(self):
        self.is_active = not self.is_active
        self.save()
