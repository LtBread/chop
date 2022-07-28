# Generated by Django 3.2.14 on 2022-07-14 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя категории')),
                ('description', models.TextField(blank=True, verbose_name='описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images')),
                ('name', models.CharField(max_length=256, verbose_name='имя продукта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('description', models.TextField(blank=True, verbose_name='описание продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('is_active', models.BooleanField(default=True, verbose_name='активно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.productcategory')),
            ],
        ),
    ]
