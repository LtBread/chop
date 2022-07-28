from django.shortcuts import HttpResponseRedirect

from productsapp.models import Product
from basketsapp.models import Basket

# Create your views here.


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(buyer=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(buyer=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
