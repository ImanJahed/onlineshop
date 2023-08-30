from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
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

            user = EP.authenticate(request, username=cd['email_or_phone_number'], password=cd['password'])
            print(user)
            if user:
                login(request, user)

                return redirect('home:index')

            else:
                if '@' in cd['email_or_phone_number']:
                    messages.error(
                        request, 'Your Email address or password incorrect')
                else:
                    messages.error(
                        request, 'Your Phone Number or password incorrect')

        return render(request, self.template_name, {'form': form})


class Dashboard(LoginRequiredMixin, View):
    form_class = DashboardForm
    template_name = 'accounts/dashboard.html'
    login_url = reverse_lazy('accounts:user_login')

    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)

        form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': form, 'profile': profile})

    def post(self, request, pk):
        user = User.objects.get(email=request.user)
        profile = Profile.objects.get(user=user)
        form = self.form_class(request.POST, instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})


class RegistrationUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = User.objects.create_user(
            email=form.cleaned_data['email'], password=form.cleaned_data['password1'])

        user.save()
        
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])

        login(self.request, user)

        profile = Profile.objects.create(user=user)

        return redirect('accounts:dash', profile.pk)
