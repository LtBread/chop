from django.urls import path

from adminsapp.views import index, admin_buyers_create, admin_buyers_read, admin_buyers_update, admin_buyers_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('buyers/', admin_buyers_read, name='buyers'),
    path('buyers-create/', admin_buyers_create, name='buyers_create'),
    path('buyers-update/', admin_buyers_update, name='buyers_update'),
    path('buyers-delete/', admin_buyers_delete, name='buyers_delete'),
]
