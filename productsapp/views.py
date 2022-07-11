from django.shortcuts import render


def index(request):
    context = {
        'title': 'Chop'
    }
    return render(request, 'productsapp/index.html', context)


def products(request):
    context = {
        'title': 'Chop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'image_url': ''},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'image_url': 'Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'image_url': ''},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00', 'description': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00', 'description': 'Гладкий кожаный верх. Натуральный материал.', 'image_url': ''},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'image_url': ''},
        ]
    }
    return render(request, 'productsapp/products.html', context)
