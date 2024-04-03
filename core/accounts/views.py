from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import CustomPasswordResetForm, LoginForm


# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = CustomPasswordResetForm

    template_name = "accounts/passwrord_rest_temp/password_rest.html"
    email_template_name = "accounts/passwrord_rest_temp/password_rest_email.html"
    subject_template_name = "accounts/passwrord_rest_temp/password_rest_subject.txt"
    success_message = (
        "We've emailed you instructions for setting your password,"
        "if an account exists with the email you entered. You should receive them shortly."
        "If you don't receive an email, "
        "please make sur you've entered the address you registered with, and check your spam folder."
    )

    success_url = reverse_lazy("website:index")
