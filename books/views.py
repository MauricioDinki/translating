from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Book
from .forms import BookForm


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book-create.html'
    success_url = reverse_lazy('books:list')


class BookDetailView(DetailView):
    model = Book
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'book'
    template_name = 'book-detail.html'


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book-list.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'category']
    success_url = reverse_lazy('books:list')
    template_name = 'book-update.html'
