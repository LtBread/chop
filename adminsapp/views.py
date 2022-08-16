from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from buyersapp.models import Buyer
from adminsapp.forms import BuyerAdminRegistrationForm


# Create your views here.


def index(request):
    context = {'title': 'Chop - Админ-панель'}
    return render(request, 'adminsapp/index.html', context)


def admin_buyers_create(request):
    if request.method == 'POST':
        form = BuyerAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('admins:buyers'))
    else:
        form = BuyerAdminRegistrationForm()
    context = {
        'title': 'Chop - Создание покупателей',
        'form': form
    }
    return render(request, 'adminsapp/admin-buyers-create.html', context)


def admin_buyers_read(request):
    context = {
        'title': 'Chop - Покупатели',
        'buyers': Buyer.objects.all()
    }
    return render(request, 'adminsapp/admin-buyers-read.html', context)


def admin_buyers_update(request):
    context = {'title': 'Chop - Редактирование покупателей'}
    return render(request, 'adminsapp/admin-buyers-update-delete.html', context)


def admin_buyers_delete(request):
    pass
