from django.urls import path

from buyersapp.views import login, registration, logout, profile

app_name = 'buyersapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
