from django import forms
from accounts.models import AddressModel
from django.utils import timezone
from order.models import CouponModel


class CheckOutForm(forms.Form):

    address_id = forms.CharField(required=True, error_messages={'required':'آدرس خود را وارد کنید'})
    coupon = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        return super().__init__(*args, **kwargs)

    def clean_address_id(self):
        address_id = self.cleaned_data.get("address_id")
        
        try:
            address = AddressModel.objects.get(user=self.request.user, id=address_id)

        except AddressModel.DoesNotExist:
            raise forms.ValidationError(" Invalid address for the requested user.")

        return address

    def clean_coupon(self):
        code = self.cleaned_data.get('coupon')

        if code == '':
            return None
        
        try:
            coupon = CouponModel.objects.get(code=code)

        except CouponModel.DoesNotExist:
            raise forms.ValidationError('کد تخفیف وارد شده صحیح نیست')
        
        if coupon.expiration_date < timezone.now():
            raise forms.ValidationError('کد مورد نظر منقضی شده است.')
        
        if coupon.used_by.count() >= coupon.max_limit_usage:

            raise forms.ValidationError("محدودیت در تعداد استفاده")
        
        if self.request.user in coupon.used_by.all():
            raise forms.ValidationError("این کد تخفیف قبلا توسط شما استفاده شده است")


        return coupon