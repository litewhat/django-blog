from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView

from articles.forms import ArticleForm

# def home(request, *args, **kwargs):
#     form = ArticleForm()
#     context = {
#         'form': form,
#         'action_url': reverse('articles:create'),
#     }
#     return render(request, 'home.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleForm()
        context['action_url'] = reverse('articles:create')
        return context
