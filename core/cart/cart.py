from shop.models import ProductModel
from .models import CartModel, CartItem

class Cart:
    def __init__(self, request) -> None:
        self.request = request

        cart = self.request.session.setdefault("cart", {})

        self.cart = cart

    def add_to_cart(self, product_id):
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += 1
        else:
            self.cart[product_id] = {"quantity": 1}

        self.save()

    def get_cart_dict(self):
        return self.cart

    def get_total_quantity(self):
        return sum([item["quantity"] for item in self.cart.values()])

    def cart_update(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id]["quantity"] = int(quantity)
        else:
            self.cart[product_id] = {"quantity": int(quantity)}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()

        products = ProductModel.objects.filter(id__in=product_ids, status=1)
        
        cart = self.cart.copy()

        for product in products:
            cart[str(product.pk)]["product"] = product

        for item in cart.values():
            item["total_product_price"] = item["product"].discount_price * item["quantity"]
            yield item

        
    def total_price(self):
        return sum([item["total_product_price"] for item in self])

    def remove_item(self, product_id):
        del self.cart[product_id]
        self.save()


    def clear(self):
        del self.request.session['cart']

        self.save()
    def sync_cart_items_from_db(self, user):
        cart, created = CartModel.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)


        for cart_item in cart_items:
            for item in self.cart:
                if str(cart_item.product.pk) == item:
                    cart_item.quantity = self.cart[item]['quantity']
                    cart_item.save()
                    break

            else:
                self.cart[str(cart_item.product.pk)] = {'quantity': cart_item.quantity}

        self.merge_session_cart_in_db(user)
        self.save()

    def merge_session_cart_in_db(self, user):
        cart, created = CartModel.objects.get_or_create(user=user)

        for item in self.cart:
            product_obj= ProductModel.objects.get(pk=item, status=1)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product_obj)
            cart_item.quantity = self.cart[item]['quantity']
            cart_item.save()
        
        session_product_ids = [item_id for item_id in self.cart]
        CartItem.objects.filter(cart=cart).exclude(product__id__in=session_product_ids).delete()


    def save(self):
        self.request.session.modified = True
