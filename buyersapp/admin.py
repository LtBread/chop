from django.contrib import admin

from buyersapp.models import Buyer
from basketsapp.admin import BasketAdmin


# Register your models here.

@admin.register(Buyer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'is_active', 'is_staff', 'is_superuser')
    inlines = BasketAdmin,
