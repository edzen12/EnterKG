from django.db import models
from apps.category.models import Category
from apps.brand.models import Brand


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='products'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sku = models.CharField(
        max_length=100,unique=True, 
        verbose_name='Артикул')
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True,null=True)
    price_usd = models.DecimalField(
        max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name