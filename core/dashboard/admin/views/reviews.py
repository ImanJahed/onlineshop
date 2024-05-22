from django.views.generic import (
    UpdateView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import FieldError

from dashboard.admin.forms.reviews import AdminReviewForm
from dashboard.permissions import HasAdminAccessPermission
from review.models import ReviewModel, ReviewStatus



class AdminReviewListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/reviews/review-list.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = ReviewModel.objects.all()

        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)

        if status := self.request.GET.get("status"):
            queryset = queryset.filter(status=status)


        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                messages.error(self.request, "ترتیب‌دهی بر اساس فیلد نامعتبر.")
                queryset = queryset.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_types'] = ReviewStatus.choices
        context['total_items'] = ReviewModel.objects.all().count()
        return context


class AdminReviewEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = 'dashboard/admin/reviews/review-edit.html'
    form_class = AdminReviewForm
    # queryset = ReviewModel.objects.all()
    model = ReviewModel
    success_message = 'تغییرات با موفقیت اعمال شد'
    # success_url = reverse_lazy('dashboard:admin:review-list')

    def get_success_url(self) -> str:
        return reverse_lazy("dashboard:admin:review-edit",kwargs={"pk":self.kwargs.get("pk")})
        # return reverse_lazy("dashboard:admin:review-edit",kwargs={"pk":self.get_object().pk})

    