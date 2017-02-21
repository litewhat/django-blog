from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.list, name='list'),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]