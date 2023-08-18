from typing import Any
from django import http
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from django.views import View

from .backends import EmailPhoneUsernameAuthenticationBackend as EP
from .forms import UserLoginForm


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

            user = EP.authenticate(request, username=cd['email_or_phone_number'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(request, "You have successfuly logged in", 'success')
                return redirect('home:index')

            else:
                if '@' in cd['email_or_phone_number']:
                    messages.error(request, 'Your Email address or password incorrect')
                else:
                    messages.error(request, 'Your Phone Number or password incorrect')




        print('errors')
        return render(request, self.template_name, {'form':form})
