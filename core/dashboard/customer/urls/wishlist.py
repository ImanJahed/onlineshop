from django.urls import path

from .. import views

urlpatterns = [
    path('wishlist/', views.CustomerWishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/delete/', views.CustomerWishlistDeleteView.as_view(), name='wishlist-delete'),
]
