from django.views.generic import TemplateView


class CustomerDashboardView(TemplateView):
    template_name = "dashboard/customer/home.html"