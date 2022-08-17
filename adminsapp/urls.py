from django.urls import path

from adminsapp.views import index, admin_buyer_create, admin_buyers, admin_buyer_update, \
    admin_buyer_change_activity, admin_products, admin_product_create, admin_product_update, \
    admin_product_change_activity, admin_categories, admin_category_create, admin_category_update, admin_category_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('buyers/', admin_buyers, name='buyers'),
    path('buyer-create/', admin_buyer_create, name='buyer_create'),
    path('buyer-update/<int:buyer_id>/', admin_buyer_update, name='buyer_update'),
    path('buyer-change-activity/<int:buyer_id>/', admin_buyer_change_activity, name='buyer_change_activity'),

    path('products/', admin_products, name='products'),
    path('product-create/', admin_product_create, name='product_create'),
    path('product-update/<int:product_id>/', admin_product_update, name='product_update'),
    path('product-change-activity/<int:product_id>/', admin_product_change_activity, name='product_change_activity'),

    path('categories/', admin_categories, name='categories'),
    path('category-create/', admin_category_create, name='category_create'),
    path('category-update/<int:category_id>/', admin_category_update, name='category_update'),
    path('category-delete/<int:category_id>/', admin_category_delete, name='category_delete'),
]
