from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'articles' # namespace for urls
urlpatterns = [
	url(r'^$', views.ArticleListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
	url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
]