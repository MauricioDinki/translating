from django.conf.urls import url

from .views import BookCreateView, BookListView, BookUpdateView

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book-list',),
    url(r'^create/$', BookCreateView.as_view(), name='book-create',),
    url(r'^update/(?P<slug>.*)/$', BookUpdateView.as_view(), name='book-update',),
]
