from django.urls import include, path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("admin/", include("dashboard.admin.urls")),
    path("customer/", include("dashboard.customer.urls")),
]
