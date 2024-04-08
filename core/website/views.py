
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin


from website.forms import ContactUsForm, NewsLetterForm
from website.models import ContactUsModel, NewsLetterModel

# Create your views here.

class Index(TemplateView):
    template_name = 'website/index.html'


class ContactUsCreateView(SuccessMessageMixin, CreateView):
    model = ContactUsModel
    form_class = ContactUsForm
    template_name = 'website/page-contact.html'
    success_url = reverse_lazy('website:contact-us')
    success_message = "درخواست شما با موفقیت ثبت شد."


class NewsLetterCreateView(SuccessMessageMixin, CreateView):
    model = NewsLetterModel
    form_class = NewsLetterForm
    success_url = reverse_lazy('website:index')
    success_message = 'ایمیل شما ثبت شد'
