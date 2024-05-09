import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .manager import UserManager
from .validators import name_validator, national_code_validator, phone_validator

# Create your models here.


class UserType(models.IntegerChoices):
    # attr =   value, label
    Customer = 1, _("Customer")
    Vendor = 2, _("Vendor")
    Admin = 3, _("Admin")
    Superuser = 4, _("Superuser")


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    type = models.IntegerField(choices=UserType.choices, default=UserType.Customer)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


def user_image_path(instance, file_name):
    return f"profile/{instance.id}/{file_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=12, blank=True, null=True)
    national_code = models.CharField(
        max_length=10, blank=True, null=True, validators=[national_code_validator]
    )
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to="profile/", default="default.jpg")

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return "کاربر جدید"

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


class AddressModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.user.email

    def get_full_address(self):
        return f"{self.state},{self.city},{self.address}"
