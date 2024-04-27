import random
import string
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# Create your models here.


class OrderStatus(models.IntegerChoices):
    pending = 1, "در انتظار پرداخت"
    processing = 2, "در حال پردازش"
    shipped = 3, "ارسال شده"
    delivered = 4, "تحویل داده شده"
    canceled = 5, "لغو شده"


class CouponModel(models.Model):
    code = models.CharField(max_length=50)
    discount_price = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    limit_usage = models.PositiveIntegerField(default=10)

    used_by = models.ForeignKey(User, on_delete=models.PROTECT)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return self.code


class OrderModel(models.Model):
    order_id = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    coupon = models.ForeignKey(
        CouponModel, on_delete=models.PROTECT, blank=True, null=True
    )
    status = models.PositiveIntegerField(
        choices=OrderStatus.choices, default=OrderStatus.pending
    )

    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"{self.user.email} - {self.order_id}"

    def _generate_random_code(self):
        rand = random.SystemRandom()
        digit_code = rand.choices(string.digits, k=6)
        return "".join(digit_code)

    def save(self, *args, **kwargs):
        if self.pk:
            return super().save(*args, **kwargs)
        
        self.order_id = f'{self.pk}-{self._generate_random_code()}'
        return super().save(*args, **kwargs)

class OrderItemModel(models.Model):
    order = models.OneToOneField(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey("shop.ProductModel", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self) -> str:
        return f"{self.product} - {self.order}"
