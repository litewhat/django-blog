from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'articles'
urlpatterns = [
	url(r'^$', views.list, name='list'),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
]