from django.contrib import admin
from apps.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active', 'sort_order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}