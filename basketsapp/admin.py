from django.contrib import admin

from basketsapp.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = 'created_timestamp',
    extra = 0
