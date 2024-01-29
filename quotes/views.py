from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


# Create your views here.
class MainPageView(View):
    template_name = 'quotes/index.html'

    def get(self, request: HttpRequest):
        return render(request, self.template_name)
