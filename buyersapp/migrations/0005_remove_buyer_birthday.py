# Generated by Django 3.2.14 on 2022-07-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyersapp', '0004_auto_20220715_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='birthday',
        ),
    ]
