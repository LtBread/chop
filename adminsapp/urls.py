from django.urls import path

from adminsapp.views import index, AdminBuyerListView, AdminBuyerCreateView, AdminBuyerUpdateView, \
    AdminBuyerChangeActivityView, AdminProductListView, AdminProductCreateView, AdminProductUpdateView, \
    AdminProductDeleteView, admin_categories, admin_category_create, admin_category_update, admin_category_delete

app_name = 'adminsapp'

urlpatterns = [
    path('', index, name='index'),

    path('buyers/', AdminBuyerListView.as_view(), name='buyers'),
    path('buyer-create/', AdminBuyerCreateView.as_view(), name='buyer_create'),
    path('buyer-update/<int:pk>/', AdminBuyerUpdateView.as_view(), name='buyer_update'),
    path('buyer-change-activity/<int:pk>/', AdminBuyerChangeActivityView.as_view(), name='buyer_change_activity'),

    path('products/', AdminProductListView.as_view(), name='products'),
    path('product-create/', AdminProductCreateView.as_view(), name='product_create'),
    path('product-update/<int:pk>/', AdminProductUpdateView.as_view(), name='product_update'),
    path('product-delete/<int:pk>/', AdminProductDeleteView.as_view(), name='product_delete'),

    path('categories/', admin_categories, name='categories'),
    path('category-create/', admin_category_create, name='category_create'),
    path('category-update/<int:category_id>/', admin_category_update, name='category_update'),
    path('category-delete/<int:category_id>/', admin_category_delete, name='category_delete'),
]
