# Generated by Django 3.2.14 on 2022-07-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersapp', '0005_remove_buyer_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='birthday',
            field=models.DateField(null=True, verbose_name='дата рождения'),
        ),
    ]
