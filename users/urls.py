from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('/login', views.LoginPageView, name='login'),
    path('/registration', views.RegistrationPageView, name='registration')
]
