from django.urls import path

from buyersapp.views import BuyerLoginView, BuyerRegistrationView, logout, profile

app_name = 'buyersapp'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('registration/', BuyerRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
