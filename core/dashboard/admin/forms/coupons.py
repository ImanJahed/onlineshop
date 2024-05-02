from django import forms

from order.models import CouponModel


class CouponForm(forms.ModelForm):

    class Meta:
        model = CouponModel
        fields = [
            "code",
            "discount_price",
            "max_limit_usage",
            "used_by",
            "expiration_date",
        ]

        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["code"].widget.attrs["class"] = "form-control"
        self.fields["discount_price"].widget.attrs["class"] = "form-control"
        self.fields["max_limit_usage"].widget.attrs["class"] = "form-control"
        # self.fields['expiration_date'].widget = forms.DateTimeInput(attrs={'type': 'date'})
        # self.fields["expiration_date"].widget.attrs["class"] = "form-control"
