from django.shortcuts import render

from productsapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Chop'
    }
    return render(request, 'productsapp/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Chop - Каталог',
        'categories': ProductCategory.objects.all,
        'products': Product.objects.all()
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    return render(request, 'productsapp/products.html', context)
