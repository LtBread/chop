from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from buyersapp.models import Buyer
from buyersapp.forms import BuyerLoginForm, BuyerRegistrationForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = BuyerLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = BuyerLoginForm()

    context = {'title': 'Chop - Авторизация', 'form': form}
    return render(request, 'buyersapp/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('buyers:login'))
    else:
        form = BuyerRegistrationForm()

    context = {'title': 'Chop - Регистрация', 'form': form}
    return render(request, 'buyersapp/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
