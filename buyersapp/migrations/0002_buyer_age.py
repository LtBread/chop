# Generated by Django 3.2.14 on 2022-07-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
            preserve_default=False,
        ),
    ]