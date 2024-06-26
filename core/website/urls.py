from django.urls import path

from . import views
app_name = 'website'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contactUs/', views.ContactUsCreateView.as_view(), name='contact'),
    path('contactUs/', views.AboutUsView.as_view(), name='about'),
    path('subscribe/', views.NewsLetterCreateView.as_view(), name='subscribe'),
]
