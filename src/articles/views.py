from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic


from .models import Article, Comment



def index(request, *args, **kwargs):
    # only for testing:
    print(args)
    print(kwargs)
    return HttpResponse('This is articles view.<br/>' + str(kwargs))



# def list(request, *args, **kwargs):
#     articles = Article.objects.all().order_by('-created')
#     #articles = None // for testing
#     #comments = [article.comments() for article in articles]
#     template = loader.get_template('articles/index.html')
#     context = {
#         'articles': articles,
#     }

#     return HttpResponse(template.render(context, request))


class ArticleListView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')


# def detail(request, article_id, *args, **kwargs):
#     #article = Article.objects.get(id=article_id)
#     article = get_object_or_404(Article, id=article_id) # it's better than that above
#     comments = article.comments().order_by('-created')
#     template = loader.get_template('articles/detail.html')

#     context = {
#         'article': article,
#         'comments': comments,
#     }

#     return HttpResponse(template.render(context, request))


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'articles/detail.html'



def comment(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments().order_by('-created')
    comment_content = request.POST.get('content')
    context = {
        'pk': article.id,
    }

    if comment_content:
        comment = Comment(article=article, content=comment_content)
        comment.save()

    return HttpResponseRedirect(reverse('articles:detail', kwargs=context))