from django.conf.urls import url

from .views import AuthorCreateView, AuthorListView

urlpatterns = [
    url(r'^$', AuthorListView.as_view(), name='list',),
    url(r'^create/$', AuthorCreateView.as_view(), name='create',),
]
