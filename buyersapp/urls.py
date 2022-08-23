from django.urls import path

from buyersapp.views import BuyerLoginView, registration, logout, profile

app_name = 'buyersapp'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
