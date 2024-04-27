from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from .tasks import send_mail


# class AuthenticationForm(auth_forms.AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         super(AuthenticationForm,self).confirm_login_allowed(user)
        
        # if not user.is_verified:
        #     raise ValidationError("user is not verified")


# Because have username field in models and in form wanna not required
class AuthenticationForm(auth_forms.AuthenticationForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(required=False)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                login(self.request, self.user_cache)

        return self.cleaned_data
# -----------------------------------------------------------------

# This Form use for celery task
class CustomPasswordResetForm(auth_forms.PasswordResetForm):
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
