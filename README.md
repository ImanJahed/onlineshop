
در این مورد دخیره کارت در دیتابیس به جای session میتونیم مدل های Cart و CartItem رو تعریف کنیم که زمانی که کاربر محصولی انتخاب کرد یک آبجکت از آن در دیتابیس ساخته شود.
در این ساختار کاربر حتما باید لاگین کرده باشد تا بتوانیم مشخص کنیم کارت برای کدوم کاربر هست

کدهای زیر نمونه هستند .


```python
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
```

```python
from django.shortcuts import render, redirect
from .models import Cart, Product, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)

   
    try:
        cart_item = CartItem.objects.get(cart=user_cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=user_cart, product=product)

    return redirect('cart_view')

@login_required
def cart_view(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    total_price = user_cart.total_price()
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(pk=item_id)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(pk=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

@login_required
def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(pk=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

```

