from django.views.generic.detail import DetailView
from .models import Author


# Create your views here.
class AuthorPageView(DetailView):
    template_name = 'authors/author-details.html'
    model = Author
    context_object_name = 'author'
