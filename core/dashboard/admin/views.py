from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from accounts.models import Profile
from dashboard.permissions import HasAdminAccessPermission
from dashboard.admin.forms import CustomePasswrodChangeForm, ProfileEditForm


class AdminDashboardView(LoginRequiredMixin, HasAdminAccessPermission, TemplateView):
    template_name = 'dashboard/admin/home.html'


class AdminSecurityEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = CustomePasswrodChangeForm
    template_name = 'dashboard/admin/security-edit.html'
    success_url = reverse_lazy('dashboard:admin:security-edit')
    success_message = 'پسورد شما با موفقیت تغییر کرد.'


class AdminProfileEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = "dashboard/admin/profile-edit.html"
    success_url = reverse_lazy('dashboard:admin:profile-edit')
    success_message = 'تغییرات شما با موفقیت ثبت شد'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)



class AdminProfileImageEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['image']
    success_url = reverse_lazy("dashboard:admin:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def form_invalid(self, form):
        messages.error(self.request, "ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)

