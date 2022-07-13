from django.urls import path

from buyersapp.views import login, logout

app_name = 'buyersapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]