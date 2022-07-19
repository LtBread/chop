from django.urls import path

from buyersapp.views import login, registration, logout

app_name = 'buyersapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]
