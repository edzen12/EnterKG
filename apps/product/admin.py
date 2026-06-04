from django.contrib import admin
from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price_usd', 'stock', 'is_active')
    list_filter = ('category', 'brand','is_active',)
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug':('name',)}