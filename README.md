# chop

python manage.py migrate
python manage.py dumpdata productsapp.ProductCategory > fixtures/categories.json
python manage.py dumpdata productsapp.Product > fixtures/products.json
python manage.py dumpdata buyersapp.Buyer > fixtures/buyers.json
python manage.py dumpdata basketsapp.Basket > fixtures/baskets.json
python manage.py loaddata 'fixtures/categories.json'
python manage.py loaddata 'fixtures/products.json'
python manage.py loaddata 'fixtures/buyers.json'
python manage.py loaddata 'fixtures/backets.json'
python manage.py createsuperuser