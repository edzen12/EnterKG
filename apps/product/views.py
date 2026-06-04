from django.views.generic import TemplateView
from apps.category.models import Category
from apps.product.models import Product

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (
            Category.objects.filter(
                parent__isnull=True, is_active=True).prefetch_related(
                    'children'
                )
        )
        context['products']= (
            Product.objects.select_related('category', 'brand').filter(
                is_active=True
            )[:12]
        )
        return context