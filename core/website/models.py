from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.validators import phone_validator


# Create your models here.
class ContactUsModel(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=60)
    phone = models.CharField(
        _("Phone"), max_length=11, validators=[phone_validator], blank=True, null=True
    )
    message = models.TextField(_("Message"))

    is_subscribed = models.BooleanField(_("Is Subscribe?"), default=False)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        user_exists = get_user_model().objects.filter(email=self.email).exists()
        if user_exists:
            self.is_subscribed = True

        return super().save(*args, **kwargs)


class NewsLetterModel(models.Model):
    email = models.EmailField(_("Email"), max_length=80)

    is_subscribed = models.BooleanField(_("Is Subscribed?"), default=False)

    class Meta:
        verbose_name = 'News letter'
        verbose_name_plural = 'News letters'

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        user_exists = get_user_model().objects.filter(email=self.email).exists()
        if user_exists:
            self.is_subscribed = True

        return super().save(*args, **kwargs)
