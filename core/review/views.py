from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import ReviewModel
from .forms import SubmitReviewForm
# Create your views here.

class SubmitReviewView(LoginRequiredMixin, CreateView):
    model = ReviewModel
    form_class = SubmitReviewForm
    http_method_names = ['post']

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        product = form.cleaned_data['product']

        messages.success(self.request, 'نظر شما ثبت شد')
        return redirect(reverse_lazy('shop:product_detail', kwargs={'slug': product.slug}))
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request,error)
        return redirect(self.request.META.get('HTTP_REFERER'))
    
    
    def get_queryset(self) -> QuerySet[Any]:
        return ReviewModel.objects.filter(user=self.request.user)
    