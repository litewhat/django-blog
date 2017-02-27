from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from articles.models import Article

class ProfileHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        if self.request.user.username == kwargs['username']:
            queryset = Article.objects.filter(user_profile__user=self.request.user)
            kwargs['articles'] = queryset
        return super().get_context_data(**kwargs)


class SettingsView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/settings.html'
    login_url = reverse_lazy('login')
    slug_field = 'username'
    slug_url_kwargs = 'username'
    quert_pk_and_slug = True
    context_object_name = 'profile'

    def get_object(self):
        return UserProfile.objects.get(user__username=self.kwargs[self.slug_url_kwargs])

    def get_success_url(self):
        return reverse_lazy('accounts:settings', kwargs=self.kwargs)