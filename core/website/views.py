from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class Index(TemplateView):
    template_name = 'website/index.html'




