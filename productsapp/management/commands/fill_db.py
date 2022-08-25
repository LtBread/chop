import os
import json
from django.core.management.base import BaseCommand

from productsapp.models import ProductCategory, Product
from buyersapp.models import Buyer
from basketsapp.models import Basket


# Путь к json-файлам, из которых восстанавливается БД
JSON_PATH = 'fixtures/'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        Product.objects.all().delete()
        ProductCategory.objects.all().delete()
        Buyer.objects.all().delete()
        Basket.objects.all().delete()

        categories = load_from_json('categories')
        products = load_from_json('products')
        buyers = load_from_json('buyers')
        baskets = load_from_json('baskets')

        for category in categories:
            ProductCategory.objects.create(id=category['pk'], **category['fields'])

        for product in products:
            category_id = product['fields']['category']
            _category = ProductCategory.objects.get(id=category_id)
            product['fields']['category'] = _category
            Product.objects.create(id=product['pk'], **product['fields'])

        Buyer.objects.create_superuser('admin', '', '1')

        for buyer in buyers:
            new_buyer = Buyer(
                id=buyer['pk'],
                password=buyer['fields']['password'],
                last_login=buyer['fields']['last_login'],
                is_superuser=buyer['fields']['is_superuser'],
                username=buyer['fields']['username'],
                first_name=buyer['fields']['first_name'],
                last_name=buyer['fields']['last_name'],
                email=buyer['fields']['email'],
                is_staff=buyer['fields']['is_staff'],
                is_active=buyer['fields']['is_active'],
                date_joined=buyer['fields']['date_joined'],
                avatar=buyer['fields']['avatar'],
                age=buyer['fields']['age']
            )
            new_buyer.groups.set(buyer['fields']['groups'])
            new_buyer.user_permissions.set(buyer['fields']['user_permissions'])
            new_buyer.save()

        for basket in baskets:
            buyer_id = basket['fields']['buyer']
            _buyer = Buyer.objects.get(id=buyer_id)
            basket['fields']['buyer'] = _buyer

            product_id = basket['fields']['product']
            _product = Product.objects.get(id=product_id)
            basket['fields']['product'] = _product

            Basket.objects.create(**basket['fields'])
