
from typing import Any, Dict
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Profile

class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required
       fields, plus a repeated password.

    """
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password2 and password1 and password1 != password2:
            raise ValidationError("Password didn`t match")

        return password2

    def save(self, commit=True):
        user =  super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            return user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text='you can change password <a href="../password">Here</a>')

    class Meta:
        model = User
        fields = ('email', _('password'), "is_active", "is_admin")


class UserLoginForm(forms.Form):
    email_or_phone_number = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())


class DashboardForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = 'user',

    def clean_usernam(self):
        username = self.cleaned_data['username']
        if Profile.objects.filter(username=username).exists():
            raise ValueError("This Username already Taken")
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise ValueError('This Phone Number already exists')
        return phone_number

