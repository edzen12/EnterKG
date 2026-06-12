from django.views.generic import TemplateView, DetailView 
from apps.category.models import Category
from apps.product.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products']= (
            Product.objects.select_related('category', 'brand').filter(
                is_active=True
            )[:12]
        )
        return context
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = (
            Product.objects.filter(
                category=self.object, is_active=True
            ).select_related(
                'brand',
                'category'
            )
        )
        return context