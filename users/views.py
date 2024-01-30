from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


# Create your views here.
class LoginPageView(View):
    template_name = "users/login.html"

    def get(self, request: HttpRequest):
        return render(request, self.template_name)


class RegistrationPageView(View):
    template_name = "users/registration.html"

    def get(self, request: HttpRequest):
        return render(request, self.template_name)