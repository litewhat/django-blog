from django.http import HttpResponse


from .models import Article


def index(request, *args, **kwargs):
    # only for testing:
    print(args)
    print(kwargs)
    return HttpResponse('This is articles view.<br/>' + str(kwargs))


def list(request, *args, **kwargs):
    articles = Article.objects.all().order_by('-created')
    html = ''
    for article in articles:
        html += '<h2>{}</h2>'.format(article.content)
        html += '<p><a href="{}">detail</a></p>'.format(article.get_absolute_url())

        for comment in article.comments():
            html += '<p>{}</p>'.format(comment.content)
        html += '<hr/>'


    return HttpResponse(html)

def detail(request, article_id, *args, **kwargs):
    article = Article.objects.get(id=article_id)
    comments = article.comments()

    html = ''
    html += '<h2>{}</h2>'.format(article.title)
    html += '<h4>{}</h4>'.format(article.content)
    html += '<h6>{}</h6>'.format(article.updated)
    html += '<hr/>'

    if comments.count() > 0:
        for comment in comments:
            html += '<h5>{}</h5>'.format(comment.content)
            html += '<h6>{}</h6>'.format(comment.content)
            html += '<hr/>'

    return HttpResponse(html)
