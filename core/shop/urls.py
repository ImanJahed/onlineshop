from django.urls import path, re_path

from . import views


app_name = 'shop'

urlpatterns = [
    path('product/grid-view/', views.ProductGridView.as_view(), name='product_grid'),
    # path('product/<slug:slug>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'product/(?P<slug>[-\w]+)/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/wishlist', views.AddAndRemoveWishListView.as_view(), name='add-or-remove-wishlist')
]
