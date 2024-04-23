from django import forms
from django.contrib.auth import forms as auth_forms

from accounts.models import Profile



class CustomePasswrodChangeForm(auth_forms.PasswordChangeForm):

    error_messages = {
        "password_incorrect": "پسورد قبلی شما اشتباه وارد شده است، لطفا تصحیح نمایید.",
        "password_mismatch": "دو پسورد ورودی با همدیگر مطابقت ندارند.",
    }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['old_password'].widget.attrs['class'] = 'form-control text-center'
    #     self.fields['new_password1'].widget.attrs['class'] = 'form-control text-center'
    #     self.fields['new_password2'].widget.attrs['class'] = 'form-control text-center'
    #     self.fields['old_password'].widget.attrs['placeholder'] = "پسورد قبلی خود را وارد نمایید"
    #     self.fields['new_password1'].widget.attrs['placeholder'] = "پسورد جایگزین خود را وارد نمایید"
    #     self.fields['new_password2'].widget.attrs['placeholder'] = "پسورد جایگزین خود را مجدد وارد نمایید"



class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'national_code']

