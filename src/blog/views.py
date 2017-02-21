from django.shortcuts import render
from django.urls import reverse

from articles.forms import ArticleForm

def home(request, *args, **kwargs):
    form = ArticleForm()
    context = {
        'form': form,
        'action_url': reverse('articles:create'),
    }
    return render(request, 'home.html', context)