from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from articles.forms import ArticleForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()
        return context