from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import HasCustomerAccessPermission

# Create your views here.
class CheckOutView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = 'order/checkout.html'