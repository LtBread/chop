from django.urls import path

from productsapp.views import products

app_name = 'productsapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page')
]
