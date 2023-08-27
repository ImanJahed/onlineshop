
import email
import profile
from typing import Any, Optional
from urllib import request
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, DetailView, FormView

from .backends import EmailPhoneUsernameAuthenticationBackend as EP
from .models import User, Profile
from .forms import UserCreationForm, UserLoginForm, DashboardForm

# USER= get_user_model()

# Create your views here.
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            user = EP.authenticate(
                request, username=cd['email_or_phone_number'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(
                    request, "You have successfuly logged in", 'success')
                return redirect('home:index')

            else:
                if '@' in cd['email_or_phone_number']:
                    messages.error(
                        request, 'Your Email address or password incorrect')
                else:
                    messages.error(
                        request, 'Your Phone Number or password incorrect')

        print('errors')
        return render(request, self.template_name, {'form': form})


class Dashboard(View):
    form_class = DashboardForm
    template_name = 'accounts/dashboard.html'

    def get(self, request,pk):
        profile = Profile.objects.get(pk=pk)

        form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': form, 'profile':profile})

    def post(self, request, pk):
        user = User.objects.get(email=request.user)
        profile = Profile.objects.get(user=user)
        form = self.form_class(request.POST, instance=profile)
        print(form)
        if form.is_valid():
            # update_profile, new_profile = Profile.objects.update_or_create(user=request.user)
            form.save()
            return render(request, self.template_name, {'form': form})
        print('invalid')
        return render(request, self.template_name, {'form': form})


# class RegistrationUserView(View):
#     def get(self, request):
#         form = UserCreationForm
#         return render(request, 'accounts/signup.html', {'form':form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password2'])
#             profile=Profile.objects.create(user=user)
#             if user:
#                 login(request, user)
#                 return redirect('accounts:dash', profile.pk)
#         return render(request, 'accounts/signup.html', {'fomr':form})

class RegistrationUserView(CreateView):
    form_class = UserCreationForm

    template_name = 'accounts/signup.html'


    def post(self, request) :
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create(email=form.cleaned_data['email'], password=form.cleaned_data['password2'])
            print(user)
            login(request, user)

            profile = Profile.objects.create(user=user)

            return redirect('accounts:dash', profile.pk)