from django.urls import path
from django.contrib.auth.decorators import login_required

from buyersapp.views import BuyerLoginView, BuyerRegistrationView, BuyerProfileView, BuyerLogoutView

app_name = 'buyersapp'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('registration/', BuyerRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(BuyerProfileView.as_view()), name='profile'),
    path('logout/', BuyerLogoutView.as_view(), name='logout'),
]
