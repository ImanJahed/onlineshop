from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('contact', views.ContacUsView.as_view(), name='contact'),
    path('about', views.AboutUsView.as_view(), name='about')
]
