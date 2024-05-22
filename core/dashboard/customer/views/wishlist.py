from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.permissions import HasCustomerAccessPermission
from shop.models import WishlistProductModel


class CustomerWishlistListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = 'dashboard/customer/wishlists/wishlist.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = WishlistProductModel.objects.filter(user=self.request.user)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(id__icontains=search_q)

        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count() 
        return context
    


class CustomerWishlistDeleteView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView):
    http_method_names = ['post']
    success_message = 'آیتم از لیست علایق شما حذف شد'
    success_url = reverse_lazy('dashboard:customer:wishlist')

    def get_queryset(self):
        return WishlistProductModel.objects.filter(user=self.request.user)