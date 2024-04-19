from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .cart import Cart


# Create your views here.
class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        cart.add_to_cart(product_id)


        return JsonResponse(
            {"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()}
        )


class UpdateCartView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")

        cart.cart_update(product_id, quantity)

        return JsonResponse(
            {"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()}
        )


class CartSummaryView(View):
    template_name = "cart/cart-summary.html"

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        context = {"cart": cart}

        return render(request, self.template_name, context)


class RemoveCartItemView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        cart.remove_item(product_id)

        return JsonResponse({'message': "Product Deleted."})
