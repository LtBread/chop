from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from productsapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Chop'
    }
    return render(request, 'productsapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'Chop - Каталог',
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'productsapp/products.html', context)
