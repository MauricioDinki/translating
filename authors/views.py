from django.views.generic import CreateView, ListView

from.models import Author


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author-create.html'
    fields = ['first_name', 'last_name']
    success_url = 'authors:list'


class AuthorListView(ListView):
    context_object_name = 'authors'
    model = Author
    template_name = 'author-list.html'
