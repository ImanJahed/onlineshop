from django import forms

from website.models import ContactUsModel, NewsLetterModel


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUsModel
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetterModel
        fields = ['email']
