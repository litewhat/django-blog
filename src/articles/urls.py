from django.conf.urls import url, include

from articles.apps import ArticlesConfig
from articles.views import *

app_name = ArticlesConfig.name

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$',
            ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update$',
            ArticleUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/comment/$',
            ArticleCommentView.as_view(), name='comment'),
    url(r'^comment/(?P<pk>[0-9]+)/like/$', 
            CommentLikeView.as_view(), name='comment-like'),
    url(r'^(?P<pk>[0-9]+)/like/$',
            ArticleLikeView.as_view(), name='like'),
    url(r'^create/$', ArticleCreateView.as_view(), name='create'),
]
