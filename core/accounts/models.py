from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


from .manager import UserManager
from .validators import phone_validator, name_validator, national_code_validator
# Create your models here.


class UserType(models.IntegerChoices):
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
    return f"{instance.id}/%Y-%m-%d/{file_name}"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True, validators=[phone_validator])
    national_code = models.CharField(max_length=10,blank=True, null=True, validators=[national_code_validator])
    first_name = models.CharField(max_length=150, null=True, blank=True, validators=[name_validator])
    last_name = models.CharField(max_length=150, null=True, blank=True, validators=[name_validator])
    profile_img = models.ImageField(upload_to=user_image_path)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            CustomerProfile.objects.create(user=instance)

