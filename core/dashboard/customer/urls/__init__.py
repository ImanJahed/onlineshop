from django.urls import path, include



app_name = 'customer'


urlpatterns = [
    path('', include('dashboard.customer.urls.profile')),
    path('', include('dashboard.customer.urls.addresses')),
]
