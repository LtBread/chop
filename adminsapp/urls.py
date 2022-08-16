from django.urls import path

from adminsapp.views import index, admin_buyers_create, admin_buyers_read, admin_buyers_update, admin_change_activity, \
    admin_products

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('buyers/', admin_buyers_read, name='buyers'),
    path('buyers-create/', admin_buyers_create, name='buyers_create'),
    path('buyers-update/<int:buyer_id>/', admin_buyers_update, name='buyers_update'),
    path('buyers-change-activity/<int:buyer_id>/', admin_change_activity, name='change_activity'),
    path('products/', admin_products, name='products'),
]
