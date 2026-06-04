from django.contrib import admin
from apps.brand.models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',  'is_active') 
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}