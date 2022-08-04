from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from productsapp.models import Product
from basketsapp.models import Basket


# Create your views here.

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(buyer=request.user, product=product)

    if product.quantity:
        if not baskets.exists():
            Basket.objects.create(buyer=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        product.quantity -= 1
        product.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.get(id=basket_id)
    product.quantity += basket.quantity
    product.save()
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
