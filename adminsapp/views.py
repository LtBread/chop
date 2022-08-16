from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from buyersapp.models import Buyer
from adminsapp.forms import BuyerAdminRegistrationForm, BuyersAdminProfileForm


# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Chop - Админ-панель'}
    return render(request, 'adminsapp/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_buyers_create(request):
    if request.method == 'POST':
        form = BuyerAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан!')
            return HttpResponseRedirect(reverse('admins:buyers'))
    else:
        form = BuyerAdminRegistrationForm()
    context = {
        'title': 'Chop - Создание покупателей',
        'form': form
    }
    return render(request, 'adminsapp/admin-buyers-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_buyers_read(request):
    context = {
        'title': 'Chop - Покупатели',
        'buyers': Buyer.objects.all()
    }
    return render(request, 'adminsapp/admin-buyers-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_buyers_update(request, buyer_id):
    selected_buyer = Buyer.objects.get(id=buyer_id)
    if request.method == 'POST':
        form = BuyersAdminProfileForm(instance=selected_buyer, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные пользователя успешно изменены!')
            return HttpResponseRedirect(reverse('admins:buyers'))
    else:
        form = BuyersAdminProfileForm(instance=selected_buyer)
    context = {
        'title': 'Chop - Редактирование покупателей',
        'form': form,
        'selected_buyer': selected_buyer
    }
    return render(request, 'adminsapp/admin-buyers-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_change_activity(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    buyer.change_activity()
    return HttpResponseRedirect(reverse('admins:buyers'))
