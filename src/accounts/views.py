from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from accounts.models import UserProfile
from articles.models import Article

class ProfileHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        if self.request.user.username == kwargs['username']:
            queryset = Article.objects.filter(user_profile__user=self.request.user)
            kwargs['articles'] = queryset
        return super().get_context_data(**kwargs)