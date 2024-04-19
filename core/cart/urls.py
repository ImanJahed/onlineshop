from django.urls import path

from . import views
app_name = 'cart'

urlpatterns = [
    path("add-to-cart/", views.AddToCartView.as_view(), name="add-to-cart"),
    path("summary/", views.CartSummaryView.as_view(), name="cart-summary"),
    path(
        "update-cart-quantity/",
        views.UpdateCartView.as_view(),
        name="update-cart-quantity",
    ),
    path(
        "remove-cart-item/", views.RemoveCartItemView.as_view(), name="remove-cart-item"
    ),
]
