from decimal import Decimal
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
    success = 2, "پرداخت شده"
    processing = 3, "در حال پردازش"
    shipped = 4, "ارسال شده"
    delivered = 5, "تحویل داده شده"
    failed = 6, "لغو شده"


class CouponModel(models.Model):
    code = models.CharField(max_length=50)
    discount_price = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    max_limit_usage = models.PositiveIntegerField(default=10)

    used_by = models.ManyToManyField(User, related_name="coupon_user", blank=True)

    expiration_date = models.DateTimeField(blank=True, null=True)
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

    payment = models.ForeignKey("payment.PaymentModel", on_delete=models.SET_NULL, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.order_id
    
    def get_status(self):
        return {
            "id":self.status,
            "title":OrderStatus(self.status).name,
            "label":OrderStatus(self.status).label,
        }


    def get_full_address(self):
        return f"{self.state},{self.city},{self.address}"


    def _generate_random_code(self):
        rand = random.SystemRandom()
        digit_code = rand.choices(string.digits, k=6)
        return "".join(digit_code)

    def save(self, *args, **kwargs):
        if self.pk:
            return super().save(*args, **kwargs)

        self.order_id = f"{self._generate_random_code()}"
        return super().save(*args, **kwargs)

    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())

    def get_price(self):
        TAX = 9 / 100

        if self.coupon:
            price_with_out_tax = self.calculate_total_price() * (1 - Decimal(self.coupon.discount_price / 100))
            price_with_tax = round(price_with_out_tax * Decimal((1 + TAX)))
            return price_with_tax

        return round(self.calculate_total_price() * Decimal((1 + TAX)))
    
    def show_price(self):
        """Showing price with separate by , in template"""

        # if self.discount_percent:
        TAX = 9 / 100

        if self.coupon:
            price_with_out_tax = self.calculate_total_price() * (1 - Decimal(self.coupon.discount_price / 100))
            price_with_tax = round(price_with_out_tax * Decimal((1 + TAX)))
            return "{:,}".format(round(price_with_tax)),
            
        return "{:,}".format(round(self.calculate_total_price() * Decimal((1 + TAX)))),

class OrderItemModel(models.Model):
    order = models.ForeignKey(
        OrderModel, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey("shop.ProductModel", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.product.title} - {self.order}"
