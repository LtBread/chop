# Generated by Django 4.1 on 2022-08-20 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0003_remove_product_categories_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productsapp.productcategory', verbose_name='категории'),
        ),
    ]
