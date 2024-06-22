from django.shortcuts import render
from django_filters.views import FilterView
from .models import Product
from .filters import ProductFilter

class ProductListView(FilterView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter