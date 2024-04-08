from datetime import timedelta
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from shop.models import ProductModel
from django.utils import timezone
from email.mime.image import MIMEImage
from django.core.mail import EmailMessage, message
from .models import NewsLetterModel


@shared_task
def send_newsletter_emails_task():
    # اینجا محصولات جدید را دریافت کنید، مثلا محصولاتی که در یک بازه زمانی اخیر اضافه شده‌اند
    some_date = timezone.now() - timedelta(days=1)  # برای مثال، محصولات اضافه شده در 24 ساعت گذشته
    new_products = ProductModel.objects.filter(status=1, display_status=1, created_at__gte=some_date)
    email_template = 'website/news_letter_email.html'
    message = render_to_string(email_template, {'products': new_products})
    subject = 'محصولات جدید در فروشگاه',

    for email in NewsLetterModel.objects.values_list('email', flat=True):
        # ایجاد محتوای ایمیل با استفاده از یک تمپلیت HTML
        # html_content = render_to_string('website/news_letter_email.html', {'products': new_products})
        # text_content = strip_tags(html_content)  # حذف تگ‌های HTML از محتوا برای نمایش متن ساده
        to_email = email
        mail = EmailMessage(subject, message, 'from@example.com', to=[to_email])
        mail.content_subtype = 'html'
        mail.send()

        # ارسال ایمیل
        # msg = EmailMultiAlternatives(
        #     'محصولات جدید در فروشگاه',
        #     text_content,
        #     'from@example.com',
        #     [email],
        # )
        # msg.attach_alternative(html_content, "text/html")

        # # اضافه کردن تصاویر به ایمیل
        # for product in new_products:
        #     with open(product.image.path, 'rb') as f:
        #         msg_img = MIMEImage(f.read())
        #         msg_img.add_header('Content-ID', '<{}>'.format(product.images.first.title))
        #         msg.attach(msg_img)
        # print('email sent', msg)
        # msg.send()
