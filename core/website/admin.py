from django.contrib import admin

from .models import ContactUsModel, NewsLetterModel


# Register your models here.

@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_subscribed']
    list_filter = ['email']


@admin.register(NewsLetterModel)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_subscribed']
