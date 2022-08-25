from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from productsapp.models import ProductCategory, Product


class MainPageView(TemplateView):
    extra_context = {'title': 'Chop'}
    template_name = 'productsapp/index.html'


# def index(request):
#     context = {
#         'title': 'Chop'
#     }
#     return render(request, 'productsapp/index.html', context)


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    extra_context = {'title': 'Chop - каталог'}
    template_name = 'productsapp/products.html'
    # allow_empty = False # редирект на стр 404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Chop - каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductCategoryListView(ProductListView):

    def get_queryset(self):
        self.category = ProductCategory.objects.get(slug=self.kwargs.get('category_slug'))
        return Product.objects.filter(category=self.category)


# def products(request, category_id=None, page=1):
#     context = {
#         'title': 'Chop - Каталог',
#         'categories': ProductCategory.objects.all()
#     }
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'productsapp/products.html', context)
