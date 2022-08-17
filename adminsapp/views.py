from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from buyersapp.models import Buyer
from productsapp.models import Product
from adminsapp.forms import AdminBuyerRegistrationForm, AdminBuyersProfileForm, AdminProductCreateForm, \
    AdminProductChangeForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Chop - Админ-панель'}
    return render(request, 'adminsapp/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_buyers(request):
    context = {
        'title': 'Chop - Покупатели',
        'buyers': Buyer.objects.all()
    }
    return render(request, 'adminsapp/buyers/admin-buyers.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_buyer_create(request):
    if request.method == 'POST':
        form = AdminBuyerRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан!')
            return HttpResponseRedirect(reverse('admins:buyers'))
    else:
        form = AdminBuyerRegistrationForm()
    context = {
        'title': 'Chop - Создание покупателей',
        'form': form
    }
    return render(request, 'adminsapp/buyers/admin-buyer-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_buyer_update(request, buyer_id):
    selected_buyer = Buyer.objects.get(id=buyer_id)
    if request.method == 'POST':
        form = AdminBuyersProfileForm(instance=selected_buyer, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные пользователя успешно изменены!')
            return HttpResponseRedirect(reverse('admins:buyers'))
    else:
        form = AdminBuyersProfileForm(instance=selected_buyer)
    context = {
        'title': 'Chop - Редактирование покупателей',
        'form': form,
        'selected_buyer': selected_buyer
    }
    return render(request, 'adminsapp/buyers/admin-buyer-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_buyer_change_activity(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    buyer.change_activity()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context = {
        'title': 'Chop - Товары',
        'products': Product.objects.all()
    }
    return render(request, 'adminsapp/products/admin-products.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар создан!')
            return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = AdminProductCreateForm()
    context = {
        'title': 'Chop - Создание товаров',
        'form': form
    }
    return render(request, 'adminsapp/products/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_update(request, product_id):
    selected_product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AdminProductChangeForm(instance=selected_product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные товара успешно изменены!')
            return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = AdminProductChangeForm(instance=selected_product)
    context = {
        'title': 'Chop - Редактирование товаров',
        'form': form,
        'selected_product': selected_product
    }
    return render(request, 'adminsapp/products/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_change_activity(request, product_id):
    product = Product.objects.get(id=product_id)
    product.change_activity()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
