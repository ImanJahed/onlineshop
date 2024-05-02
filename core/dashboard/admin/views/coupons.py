from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from order.models import CouponModel
from dashboard.permissions import HasAdminAccessPermission
from ..forms import CouponForm


class AdminCouponListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    queryset = CouponModel.objects.all()
    template_name = 'dashboard/admin/coupons/coupon-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_items'] = CouponModel.objects.count()
        return context


class AdminCouponCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    form_class = CouponForm
    template_name = 'dashboard/admin/coupons/coupon-create.html'
    success_message = 'کد تخفیف با موفقیت ایجاد شد'
    success_url = reverse_lazy('dashboard:admin:coupon-list')
    
    def get_queryset(self):
        return CouponModel.objects.all()
    


class AdminCouponEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    form_class = CouponForm
    template_name = 'dashboard/admin/coupons/coupon-edit.html'
    success_message = 'کد تخفیف با موفقیت ویرایش شد'
    model = CouponModel

    def get_success_url(self):
        return reverse_lazy('dashboard:admin:coupon-edit', kwargs={'pk': self.get_object().pk})
    

class AdminCouponDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = 'dashboard/admin/coupons/coupon-delete.html'
    success_message = 'کد تخفیف با موفقیت حذف شد'
    success_url = reverse_lazy('dashboard:admin:coupon-list')
    model = CouponModel