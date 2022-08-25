from django.urls import path

from productsapp.views import ProductListView, ProductCategoryListView

app_name = 'productsapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug:category_slug>/', ProductCategoryListView.as_view(), name='category'),
    # path('page/<int:page>/', products, name='page')
]
