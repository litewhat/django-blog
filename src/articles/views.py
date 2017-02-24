from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Article, Comment
from .forms import ArticleForm
from accounts.models import UserProfile


class ArticleListView(ListView):
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'


class ArticleCommentView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['pk'])
        context = {
            'pk': article.id,
        }
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=context)
                                    )

    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        article = get_object_or_404(Article, id=kwargs['pk'])
        comment_content = request.POST.get('content')
        context = {
            'pk': article.id,
        }
        if comment_content is not None:
            comment = Comment(user_profile=user_profile, article=article,
                              content=comment_content)
            comment.save()
        return HttpResponseRedirect(reverse_lazy(
                                        'articles:detail', kwargs=context)
                                    )


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Article
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