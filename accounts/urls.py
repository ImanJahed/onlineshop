from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='user_login'),
    path('signup', views.RegistrationUserView.as_view(), name='signup'),
    path('dashboard/<int:pk>', views.Dashboard.as_view(), name='dash'),


]
