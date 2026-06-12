from django.db.models import Count, Prefetch
from apps.category.models import Category



def sidebar_categories(request):
    categories = (Category.objects.filter(
                parent__isnull=True,is_active=True
            ).prefetch_related(
                Prefetch(
                    'children',
                    queryset=Category.objects.annotate(
                        products_count=Count('products')
                    )
                )
            )
        )
    return {
        "sidebar_categories":categories
    }
    