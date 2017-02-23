from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm
from articles.forms import ArticleForm


class HomePageView(TemplateView):
    template_name = 'home.html'
    query_string = True


    def get(self, request):
        if request.GET:
            # it can be passed in the future in searching form
            print(request.GET['q'])
        return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()

        return context


class UserRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def render_to_response(self, context, **response_kwargs):
        # When user is logged in it should redirect to homepage.
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().render_to_response()