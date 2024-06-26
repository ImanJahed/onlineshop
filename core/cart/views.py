from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .cart import Cart


# Create your views here.


class CartSummaryView(View):
    template_name = "cart/cart-summary.html"

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        context = {"cart": cart}

        return render(request, self.template_name, context)


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        cart.add_to_cart(product_id)

        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)

        return JsonResponse(
            {"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()}
        )


class UpdateCartView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")

        cart.cart_update(product_id, quantity)

        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)

        return JsonResponse(
            {"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()}
        )


class RemoveCartItemView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        cart.remove_item(product_id)

        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)

        return JsonResponse({"message": "Product Deleted."})
