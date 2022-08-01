from django.db import models

from buyersapp.models import Buyer
from productsapp.models import Product


# Create your models here.


class Basket(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Корзина для {self.buyer.username} | Продукт {self.product.name}'

    @property
    def baskets(self):
        return Basket.objects.filter(buyer=self.buyer)

    def sum(self):
        return self.product.price * self.quantity

    def total_sum(self):
        return sum(basket.sum() for basket in self.baskets)

    def total_quantity(self):
        return sum(basket.quantity for basket in self.baskets)
