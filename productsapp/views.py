from django.shortcuts import render


def index(request):
    context = {
        'title': 'Chop'
    }
    return render(request, 'productsapp/index.html', context)


def products(request):
    context = {
        'title': 'Chop - Каталог'
    }
    return render(request, 'productsapp/products.html', context)
