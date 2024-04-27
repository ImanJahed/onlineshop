from django.db import models
from django.contrib.auth import get_user_model

from shop.models import ProductModel


User = get_user_model()


# Create your models here.
class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.user.email 


class CartItem(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product} - {self.cart}"
