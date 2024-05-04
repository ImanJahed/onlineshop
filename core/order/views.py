from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from cart.models import CartItem, CartModel
from accounts.models import AddressModel
from payment.models import PaymentModel
from order.models import CouponModel, OrderItemModel, OrderModel
from .permissions import HasCustomerAccessPermission
from .forms import CheckOutForm
from payment.zarinpal_client import ZarinPalSandBox

# Create your views here.
class OrderCheckOutView(LoginRequiredMixin, HasCustomerAccessPermission, FormView):
    template_name = "order/checkout.html"
    form_class = CheckOutForm
    success_url = reverse_lazy("order:completed")

    def form_valid(self, form):
        cart = CartModel.objects.get(user=self.request.user)

        cd = form.cleaned_data
        address = cd.get("address_id")
        code = cd.get("coupon")

        order_obj = self.create_order(address)

        self.create_order_items(order_obj, cart)

        if code:
            self.apply_coupon(order_obj, code)

        order_obj.total_price = order_obj.get_price()
        order_obj.save()

        payment_url = self.create_payment(order_obj)

        return redirect(payment_url)

    def create_order(self, address):
        """Cerate Object of Order Model"""
        return OrderModel.objects.create(
            user=self.request.user,
            address=address.address,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
        )

    def create_order_items(self, order, cart):
        """Create Order Items for Order from Cart Items"""
        for item in cart.cart_items.all():
            OrderItemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.discount_price,
            )

    def apply_coupon(self, order, coupon):
        """Apply Coupon on order object"""
        order.coupon = coupon
        order.save()

        coupon.used_by.add(self.request.user)
        coupon.save()

    def create_payment(self, order):
        zarinpal = ZarinPalSandBox()

        response = zarinpal.payment_request(int(order.total_price))
        page_url =zarinpal.generate_payment_url(response.get('Authority'))

        payment_obj = PaymentModel.objects.create(
            authority_id=response.get('Authority'),
            amount=order.total_price
        )
        order.payment = payment_obj
        order.save()

        return page_url
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = AddressModel.objects.filter(user=self.request.user)
        context["total_price"] = round(cart.calculate_total_price() * (1 + 9 / 100))
        context["total_tax"] = round(cart.calculate_total_price() * 9 / 100)

        return context


class ValidateCouponView(LoginRequiredMixin, HasCustomerAccessPermission, View):
    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        message = "کد تخفیف با موفقیت ثبت شد"
        status_code = 200
        total_price = 0
        total_tax = 0

        try:
            coupon = CouponModel.objects.get(code=code)

        except CouponModel.DoesNotExist:
            message, status_code = "کد تخفیف وارد شده صحیح نیست", 404

        else:
            if coupon.expiration_date < timezone.now():
                message, status_code = "کد مورد نظر منقضی شده است.", 403

            elif coupon.used_by.count() >= coupon.max_limit_usage:
                message, status_code = "محدودیت در تعداد استفاده", 403

            elif self.request.user in coupon.used_by.all():
                message, status_code = "این کد تخفیف قبلا توسط شما استفاده شده است", 403

            else:
                cart = CartModel.objects.get(user=request.user)
                price = cart.calculate_total_price()
                total_price_with_out_tax = round(price * (1 - Decimal(coupon.discount_price / 100)))
                total_tax = round(total_price_with_out_tax * (Decimal(9 / 100)))

                total_price = total_tax + total_price_with_out_tax

        return JsonResponse(
            {"message": message, "total_price": total_price, "total_tax": total_tax},
            status=status_code,
        )


class OrderCompletedView(TemplateView):
    template_name = "order/completed.html"

class OrderFailedView(TemplateView):
    template_name = "order/failed.html"