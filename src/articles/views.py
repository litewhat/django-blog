from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Article, Comment
from .forms import ArticleForm



class ArticleListView(ListView):
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'



class CommentArticleView(View):

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['pk'])
        comments = article.comments().order_by('-created')
        comment_content = request.POST.get('content')
        context = {
            'pk': article.id,
        }

        if comment_content:
            comment = Comment(article=article, content=comment_content)
            comment.save()
        return HttpResponseRedirect(reverse_lazy('articles:detail', kwargs=context))



class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    success_url = reverse_lazy('articles:list')
