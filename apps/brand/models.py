from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(
        upload_to='brands/',
        blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Бренды'
        verbose_name = 'бренд'

    def __str__(self):
        return self.name