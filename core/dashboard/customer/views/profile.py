from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from dashboard.customer.forms.profile import CustomerPasswordChangeForm, CustomerProfileEditForm
from dashboard.permissions import HasCustomerAccessPermission
from accounts.models import Profile



class CustomerDashboardView(TemplateView):
    template_name = "dashboard/customer/profile/home.html"



class CustomerSecurityEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = CustomerPasswordChangeForm
    template_name = 'dashboard/customer/profile/security-edit.html'
    success_url = reverse_lazy('dashboard:customer:security-edit')
    success_message = 'پسورد شما با موفقیت تغییر کرد.'




class CustomerProfileEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/customer/profile/profile-edit.html"
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)



class CustomerProfileImageEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)