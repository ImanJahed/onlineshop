from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, 'home/index.html')



class ContacUsView(View):
    template_name = 'home/contact.hmtl'
    form_class = ContactForm

    def get(self,request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message successfuly sent")

        return render(request, self.template_name, {'form': form})



class AboutUsView(TemplateView):
    template_name = 'home/about.html'