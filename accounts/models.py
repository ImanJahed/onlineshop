from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name=_('Email Address'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Admin'))
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    def has_module_perms(self, app_lable):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin



class Profile(models.Model):
    """
      A profile for each user

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11, unique=True, verbose_name=_('Phone Number'))
    image = models.ImageField(upload_to='img/profie')
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        if self.username:
            return self.username
        return self.phone_number

