from django.shortcuts import render

from buyersapp.models import Buyer


# Create your views here.


def index(request):
    context = {'title': 'Chop - Админ-панель'}
    return render(request, 'adminsapp/index.html', context)


def admin_buyers_create(request):
    context = {'title': 'Chop - Создание покупателей'}
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
