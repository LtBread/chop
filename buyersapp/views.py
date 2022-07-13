from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from buyersapp.models import Buyer
from buyersapp.forms import BuyerLoginForm


# Create your views here.

def login(request):
    form = BuyerLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active():
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    context = {
        'title': 'Chop - Авторизация',
        'form': form,
    }

    return render(request, 'buyersapp/login.html', context)


def registration(request):
    context = {'title': 'Chop - Регистрация'}
    return render(request, 'buyersapp/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
