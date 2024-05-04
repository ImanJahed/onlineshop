from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View

from cart.models import CartModel
from order.models import OrderModel
from .models import PaymentModel
from cart.cart import Cart
from .zarinpal_client import ZarinPalSandBox
# Create your views here.
class PaymentVerifyView(View):

    def get(self, request, *args, **kwargs):
        status = request.GET.get('Status')
        ref_id = request.GET.get('RefID')
        authority_id = request.GET.get('Authority')
        payment_obj = get_object_or_404(PaymentModel, authority_id=authority_id)
        zarinpal = ZarinPalSandBox()
        response = zarinpal.payment_verify(amount=int(payment_obj.amount), authority=payment_obj.authority_id)

        if response.get('Status') == 100 or response.get('Status') == 101: 
            payment_obj.ref_id = response.get('RefID')
            payment_obj.response_code = response.get('Status')
            payment_obj.response_json = response
            payment_obj.status = 2
            payment_obj.save()
            order = OrderModel.objects.get(payment=payment_obj)
            order.status = 2
            order.save()

            # Clear Cart session and Cart Item in database
            Cart(request).clear()
            cart = CartModel.objects.get(user=request.user)
            cart.cart_items.all().delete()

            # Decrease Product Stock
            for item in order.order_items.all():
                item.product.stock -= item.quantity
                item.product.save()

            return redirect('order:completed')
        
        else:
            payment_obj.ref_id = response.get('RefID')
            payment_obj.response_code = response.get('Status')
            payment_obj.response_json = response
            payment_obj.status = 3
            payment_obj.save()

            order = OrderModel.objects.get(payment=payment_obj)
            order.status = 6
            if order.coupon:
                order.coupon.used_by.remove(request.user)
                order.coupon = None
            order.save()

            return redirect('order:failed')