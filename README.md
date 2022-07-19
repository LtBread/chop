# chop

python manage.py migrate
python manage.py dumpdata productsapp.ProductCategory > categories.json
python manage.py dumpdata productsapp.Product > products.json
python manage.py loaddata 'productsapp/fixtures/categories.json'
python manage.py loaddata 'productsapp/fixtures/products.json'
python manage.py createsuperuser