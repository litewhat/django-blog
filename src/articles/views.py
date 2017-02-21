from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic


from .models import Article, Comment
from .forms import ArticleForm



class ArticleListView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')



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



def create(request, *args, **kwargs):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            data_dict = form.clean()
            title = data_dict['title']
            content = data_dict['content']
            article = Article(title=title, content=content)
            article.save()
            return HttpResponseRedirect(reverse('articles:list'))
    else:
        form = ArticleForm()
        context = {
            'form': form,
            'action_url': reverse('articles:create')
        }

    return render(request, 'articles/create_article.html', context)