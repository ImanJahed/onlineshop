from django.contrib import admin
from .models import OrderModel, OrderItemModel, CouponModel


# Register your models here.
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_id",
        "user",
        "total_price",
        "coupon",
        "status",
        "created_date",
    ]
    list_editable = ["status"]
    search_fields = ["user"]
    list_filter = ['status']

@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "product",
        "quantity",
        "price",
        "created_date",
    ]

    search_fields = ["order"]


@admin.register(CouponModel)
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "discount_price",
        "max_limit_usage",
        'used_by_count',
        'expiration_date',
        "created_date",
    ]

    def used_by_count(self, obj):
        return obj.used_by.all().count()