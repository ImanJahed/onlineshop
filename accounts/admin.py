from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


# Register your models here.
class UserAdmin(UserBaseAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'is_admin']
    list_filter = ['is_admin']


    fieldsets = (
        (_('Personal Info'), {'fields':(('email', 'password'))}),
        (_('Permissions'), {'fields':('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':['wide'],
            'fields': ('email', 'password1', 'password2')}),
    )

    ordering = ["email"]
    search_fields = ("email",)
    filter_horizontal = []


admin.site.register(User, UserAdmin)

# Since, we'er are not using Django's built-in permissions,
# Unregisterd Group model from admin
admin.site.unregister(Group)