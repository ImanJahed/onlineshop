from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from review.models import ReviewModel

from .models import ProductModel, ProductCategoryModel, WishlistProductModel

# Create your views here.


class ProductGridView(ListView):
    template_name = 'shop/products-grid.html'
    paginate_by = 9

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
        context['wishlist_items'] = WishlistProductModel.objects.filter(user=self.request.user).values_list('product__id', flat=True) if self.request.user.is_authenticated else False
        return context


class ProductDetailView(DetailView):
    queryset = ProductModel.objects.filter(status=1, display_status=1)
    template_name = 'shop/product-detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        product = self.get_object()
        context["is_wished"] = WishlistProductModel.objects.filter(
            user=self.request.user, product__id=product.pk).exists() if self.request.user.is_authenticated else False
        reviews = ReviewModel.objects.filter(product=product, status=2).order_by('-created_at')
        context['reviews'] = reviews
        total_review_count = reviews.count()

        context['reviews_count'] = {
            f"rate_{rate}": reviews.filter(rate=rate).count for rate in range(1,6)
        }

        if total_review_count != 0:
            context['reviews_avg'] = {
                f"rate_{rate}": round((reviews.filter(rate=rate).count() / total_review_count)* 100 , 2) for rate in range(1, 6)
            }

        else:
            context['reviews_avg'] = {f"rate_{rate}": 0 for rate in range(1, 6)}
        return context
    


class AddAndRemoveWishListView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        message = ''

        if product_id:
            try:
                wishlist_item = WishlistProductModel.objects.get(user=request.user, product_id=product_id)
                wishlist_item.delete()
                message = 'محصول از لیست علایق حذف شد'
            
            except WishlistProductModel.DoesNotExist:
                WishlistProductModel.objects.create(
                    user=request.user,
                    product_id=product_id
                )
                message = 'محصول به لیست علایق اضافه شد'

        return JsonResponse({'message': message})