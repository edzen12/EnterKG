from django.urls import path
from apps.product.views import HomeView, CategoryDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('category/<slug:slug>/',
         CategoryDetailView.as_view(),name='category_detail'
    ),
]
