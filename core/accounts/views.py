from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomPasswordResetForm

from .forms import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        super().get_default_redirect_url()

        if self.next_page:
            return resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            return resolve_url("website:index")



from django.conf import settings


class LogoutView(auth_views.LogoutView):
    """Set LOGOUT_REDIRECT_URL for redirect user after logout without showing a logout template"""
    pass


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    # form_class = CustomPasswordResetForm ==> If use celery uncomment this code

    template_name = 'accounts/page-reset-password-simple.html'
    email_template_name = 'accounts/password_reset_temp/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_temp/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password,"\
                      "if an account exists with the email you entered. You should receive them shortly."\
                      "If you don't receive an email, " \
                      "please make sur you've entered the address you registered with, and check your spam folder."

    success_url = reverse_lazy('website:index')
