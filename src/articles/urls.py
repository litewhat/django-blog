from django.conf.urls import url, include
from django.contrib import admin

from .views import ArticleListView, ArticleDetailView, ArticleCommentView, ArticleCreateView, ArticleUpdateView

app_name = 'articles' # namespace for urls
urlpatterns = [
	url(r'^$', ArticleListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/update$', ArticleUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>[0-9]+)/comment/$', ArticleCommentView.as_view(), name='comment'),
	url(r'^create/$', ArticleCreateView.as_view(), name='create'),
]