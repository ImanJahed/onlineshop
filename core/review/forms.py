from django import forms

from .models import ReviewModel
from shop.models import ProductModel

class SubmitReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewModel
        fields = ['product','comment', 'rate']

        error_messages = {
            'description': {
                'required': 'فیلد توضیحات اجباری است',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')

        # Check if the product exists and is published
        try:
            ProductModel.objects.get(id=product.pk, status=1, display_status=1)

        except ProductModel.DoesNotExist:
            raise forms.ValidationError("این محصول وجود ندارد")

        return cleaned_data
    
