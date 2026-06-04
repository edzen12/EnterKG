from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        verbose_name="Родительская категория"
    )
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='category/', blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'