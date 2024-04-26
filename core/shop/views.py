
from django.views.generic import ListView, DetailView

from .models import ProductModel, ProductCategoryModel

# Create your views here.


class ProductGridView(ListView):
    template_name = 'shop/products-grid.html'
    paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        qs = ProductModel.objects.filter(status=1, display_status=1)

        if order_by := self.request.GET.get('order_by'):
            qs = qs.order_by(order_by)

        if q := self.request.GET.get('q'):
            qs = qs.filter(title__icontains=q)

        if max_price := self.request.GET.get('max_price'):
            qs = qs.filter(price__lte=max_price)

        if min_price := self.request.GET.get('min_price'):
            qs = qs.filter(price__gte=min_price)

        if categories := self.request.GET.get('categories'):
            print(categories)
            qs = qs.filter(categories__title=categories)
   
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_product'] = self.get_queryset().count()
        context['categories'] = ProductCategoryModel.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = ProductModel.objects.filter(status=1, display_status=1)
    template_name = 'shop/product-detail.html'
