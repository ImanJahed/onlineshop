from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from celery import shared_task


@shared_task
def send_mail(subject_template_name, email_template_name, context,
              from_email, to_email, html_email_template_name):
    context['user'] = get_user_model().objects.get(email=context['user'])

    PasswordResetForm.send_mail(None, subject_template_name,
                                email_template_name, context,
                                from_email, to_email,
                                html_email_template_name)
