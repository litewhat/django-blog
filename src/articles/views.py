from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse


from .models import Article, Comment



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
    comments = article.comments().order_by('-created')
    template = loader.get_template('articles/detail.html')

    context = {
        'article': article,
        'comments': comments,
    }

    return HttpResponse(template.render(context, request))



def comment(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments()
    comment_content = request.POST.get('content')
    context = {
        'article_id': article.id,
        # 'article': article,
        # 'comments': comments,
    }
    error_message = ''

    if not comment_content:
        pass
        # error_message = 'This field cannot be empty.'
        # context['error_message'] = error_message
    else :
        comment = Comment(article=article, content=comment_content)
        comment.save()

    return HttpResponseRedirect(reverse('articles:detail', kwargs=context))