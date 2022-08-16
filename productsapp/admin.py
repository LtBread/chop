from django.contrib import admin

from productsapp.models import ProductCategory, Product

# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('category', 'name', 'description', ('price', 'quantity'), 'image')
    readonly_fields = ('description',)
    ordering = ('name', '-price')
    search_fields = 'name',
