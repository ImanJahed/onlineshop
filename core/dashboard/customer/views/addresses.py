from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from accounts.models import AddressModel
from dashboard.customer.forms.addresses import UserAddressForm


class CustomerAddressListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/addresses/address-list.html"

    def get_queryset(self):
        return AddressModel.objects.filter(user=self.request.user)


class CustomerAddressCreateView(
    LoginRequiredMixin, HasCustomerAccessPermission, CreateView, SuccessMessageMixin
):
    form_class = UserAddressForm
    template_name = "dashboard/customer/addresses/address-create.html"
    success_message = "آدرس با موفقیت ثبت شد"

    def get_queryset(self):
        return AddressModel.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        # return redirect("dashboard:customer:address-edit", kwargs={"pk": self.form.instance.pk})

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:customer:address-edit", kwargs={"pk": self.object.pk}
        )


class CustomerAddressEditView(
    LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, UpdateView
):
    form_class = UserAddressForm
    template_name = "dashboard/customer/addresses/address-edit.html"
    success_message = "تغییرات با موفقیت ثبت شد"

    def get_queryset(self):
        return AddressModel.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:customer:address-edit", kwargs={"pk": self.get_object().pk}
        )


class CustomerAddressDeleteView(
    LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView
):
    template_name = "dashboard/customer/addresses/address-delete.html"
    success_message = "آدرس با موفقیت حذف شد"

    def get_queryset(self):
        return AddressModel.objects.filter(user=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:customer:address-list')