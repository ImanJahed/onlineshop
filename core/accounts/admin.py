from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Profile

# Register your models here.
User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["username", "email", "type"]
    list_filter = ["type"]
    search_fields = ["username", "email"]
    filter_vertical = []

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ("Authentication", {"fields": ("username", "email", "password")}),
        (
            "Permission",
            {"fields": ("is_staff", "is_active", "is_verified", "is_admin")},
        ),
        ("Group Permission", {"fields": ("groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
        "phone",
        "user_type",
        "user_username",
    ]
    search_fields = ["first_name", "last_name", "phone"]

    def user_type(self, obj):
        """
        Show specific field in user model to profile admin model
        get_{field_name}_display() for choice field using
        """
        return obj.user.get_type_display()

    user_type.short_description = "Type"  # Change display name in admin panel

    def user_username(self, obj):
        """Display specific field on user model."""
        return obj.user.username

    user_username.short_description = "Username"


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
