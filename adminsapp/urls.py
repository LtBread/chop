from django.urls import path

from adminsapp.views import AdminPanelView, AdminBuyerListView, AdminBuyerCreateView, AdminBuyerUpdateView, \
    AdminBuyerChangeActivityView, AdminProductListView, AdminProductCreateView, AdminProductUpdateView, \
    AdminProductDeleteView, AdminCategoryListView, AdminCategoryCreateView, AdminCategoryUpdateView, AdminCategoryDeleteView

app_name = 'adminsapp'

urlpatterns = [
    path('', AdminPanelView.as_view(), name='index'),

    path('buyers/', AdminBuyerListView.as_view(), name='buyers'),
    path('buyer-create/', AdminBuyerCreateView.as_view(), name='buyer_create'),
    path('buyer-update/<int:pk>/', AdminBuyerUpdateView.as_view(), name='buyer_update'),
    path('buyer-change-activity/<int:pk>/', AdminBuyerChangeActivityView.as_view(), name='buyer_change_activity'),

    path('products/', AdminProductListView.as_view(), name='products'),
    path('product-create/', AdminProductCreateView.as_view(), name='product_create'),
    path('product-update/<int:pk>/', AdminProductUpdateView.as_view(), name='product_update'),
    path('product-delete/<int:pk>/', AdminProductDeleteView.as_view(), name='product_delete'),

    path('categories/', AdminCategoryListView.as_view(), name='categories'),
    path('category-create/', AdminCategoryCreateView.as_view(), name='category_create'),
    path('category-update/<int:pk>/', AdminCategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<int:pk>/', AdminCategoryDeleteView.as_view(), name='category_delete'),
]
