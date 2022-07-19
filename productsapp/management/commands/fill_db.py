import os
import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from productsapp.models import ProductCategory, Product
from buyersapp.models import Buyer

# Скрипт не работает из-за foreign key. При создании продукта он ссылается на несуществующее поле name.
# На момент создания продукта ключ к категории является уже устаревшим.

# Путь к json-файлам, из которых восстанавливается БД
JSON_PATH = 'productsapp/json/'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category['fields'])
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['fields']['category']
            _category = ProductCategory.objects.get(name=category_name)  # вот тут
            product['fields']['category'] = _category
            new_product = Product(**product['fields'])
            new_product.save()

        superuser = Buyer.objects.create_superuser('admin', '', '1')
