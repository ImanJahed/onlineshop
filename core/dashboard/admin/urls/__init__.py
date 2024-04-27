from django.urls import path, include


app_name = 'admin'

urlpatterns = [
    path('', include('dashboard.admin.urls.profile')),
    path('', include('dashboard.admin.urls.products')),

]