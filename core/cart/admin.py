from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import CartModel, CartItem

# Register your models here.
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ["session_key", "_session_data", "expire_date"]


admin.site.register(CartModel)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']