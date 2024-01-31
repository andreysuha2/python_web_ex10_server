from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('author/<int:pk>', views.AuthorPageView.as_view(), name='details')
]
