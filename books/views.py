from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Book


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'category']
    template_name = 'book-create.html'
    success_url = reverse_lazy('books:book-list')


class BookListView(ListView):
    context_object_name = 'books'
    model = Book
    page_kwarg = 'page'
    paginate_by = 10
    template_name = 'book-list.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'category']
    success_url = reverse_lazy('books:book-list')
    template_name = 'book-update.html'
