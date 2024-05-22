from django import forms

from review.models import ReviewModel

class AdminReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['comment', 'rate', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        self.fields['rate'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
