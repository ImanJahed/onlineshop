from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# app_name = "accounts"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password-rest/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "password-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/passwrord_rest_temp/password_rest_confirm.html"
        ),
        name="password_rest_confirm",
    ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_temp/password_reset_complete.html'),
         name='password_reset_complete'),
]
