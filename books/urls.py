from django.conf.urls import url

from .views import BookCreateView, BookDetailView, BookListView, BookUpdateView

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='list',),
    url(r'^create/$', BookCreateView.as_view(), name='create',),
    url(r'^detail/(?P<slug>.*)/$', BookDetailView.as_view(), name='detail',),
    url(r'^update/(?P<slug>.*)/$', BookUpdateView.as_view(), name='update',),
]
