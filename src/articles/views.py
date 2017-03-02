from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from articles.models import Article, Comment
from articles.forms import ArticleForm
from accounts.models import UserProfile


class ArticleMixin(object):
    model = Article


class ArticleListView(ArticleMixin, ListView):
    template_name = 'articles/index.html'
    context_object_name = 'articles'


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'articles/detail.html'


class ArticleCreateView(LoginRequiredMixin, ArticleMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        article = form.instance
        qs = UserProfile.objects.filter(user=self.request.user)
        if qs.count() == 1:
            user_profile = qs.first()
        article.user_profile = user_profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update_article.html'
    success_url = reverse_lazy('articles:list')

    def dispatch(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        # authorization
        if request.user == article.user_profile.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:list'))


class ArticleCommentView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['pk'])
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=kwargs))

    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        article = get_object_or_404(Article, id=kwargs['pk'])
        comment_content = request.POST['content']
        if comment_content:
            comment = Comment(user_profile=user_profile, article=article,
                              content=comment_content)
            comment.save()
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=kwargs))


class ArticleLikeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        article = get_object_or_404(Article, id=kwargs['pk'])
        if article in user_profile.liked_articles.all():
            user_profile.liked_articles.remove(article)
        else:
            user_profile.liked_articles.add(article)
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=kwargs))


class CommentLikeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        comment = get_object_or_404(Comment, id=kwargs['pk'])
        article = comment.article
        if comment in user_profile.liked_comments.all():
            user_profile.liked_comments.remove(comment)
        else:
            user_profile.liked_comments.add(comment)
        kwargs['pk'] = article.id
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=kwargs))