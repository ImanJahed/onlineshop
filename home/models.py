from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contact(models.Model):
    """
    A model for save user contact

    """

    name = models.CharField(max_length=50, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(max_length=11, blank=True, verbose_name=_("Phone Number"))
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return self.email