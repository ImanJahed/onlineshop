
from django.shortcuts import redirect
from django.views.generic import View


# Create your views here.
class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        if request.user.is_authenticated and request.user.type == 1: # type: ignore
            return redirect('dashboard:customer:home')
        else:
            return redirect('dashboard:admin:home')
        