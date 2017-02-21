from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader


from .models import Article



def index(request, *args, **kwargs):
    # only for testing:
    print(args)
    print(kwargs)
    return HttpResponse('This is articles view.<br/>' + str(kwargs))



def list(request, *args, **kwargs):
    articles = Article.objects.all().order_by('-created')
    #articles = None // for testing
    #comments = [article.comments() for article in articles]
    template = loader.get_template('articles/index.html')
    context = {
        'articles': articles,
    }

    return HttpResponse(template.render(context, request))



def detail(request, article_id, *args, **kwargs):
    #article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id) # it's better than that above
    comments = article.comments()
    template = loader.get_template('articles/detail.html')

    context = {
        'article': article,
        'comments': comments,
    }

    return HttpResponse(template.render(context, request))



def comment(request, article_id, *args, **kwargs):
    pass