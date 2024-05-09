from django.urls import path

from .. import views


urlpatterns = [
    path('order/list/', views.CustomerOrderListView.as_view(), name='order-list'),
    path('order/detail/<int:pk>/', views.CustomerOrderDetailView.as_view(), name='order-detail'),
]
