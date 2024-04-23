from shop.models import ProductModel


class Cart:

    def __init__(self, request) -> None:
        self.request = request
        
        cart = self.request.session.setdefault('cart', {})

        self.cart = cart


    def add_to_cart(self, product_id):
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += 1
        else:
            self.cart[product_id] = {'quantity': 1}

        self.save()

    def get_cart_dict(self):
        return self.cart

    def get_total_quantity(self):
        return sum([item['quantity'] for item in self.cart.values()])

    def cart_update(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id] = {'quantity': int(quantity)}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.pk)]['product'] = product
            
        for item in cart.values():
            item['total_product_price'] = item['product'].price * item['quantity']
            yield item

    def total_price(self):
        return sum([item['total_product_price'] for item in self])

    def remove_item(self, product_id):
        del self.cart[product_id]
        self.save()
        
    def save(self):
        self.request.session.modified = True

