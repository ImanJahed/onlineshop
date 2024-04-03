from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.exceptions import ValidationError

from .tasks import send_mail


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user: AbstractBaseUser) -> None:
        super().confirm_login_allowed(user)

        if not user.is_verified:
            raise ValidationError('User is not Verified.')


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Email'
        }
    ))

    def send_mail(self, subject_template_name, email_template_name, context,
                  from_email, to_email, html_email_template_name=None):

        context['user'] = context['user'].email

        send_mail.delay(subject_template_name, email_template_name, context,
                        from_email, to_email, html_email_template_name=None)
