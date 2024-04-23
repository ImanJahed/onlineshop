from .cart import Cart


def test_cart(request):
    cart = Cart(request)

    return {'cart': cart, 'total_quantity': cart.get_total_quantity()}