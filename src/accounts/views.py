from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class ProfileHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'accounts/profile.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return super().dispatch(request, *args, **kwargs)
    #     return Http404()
