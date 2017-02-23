from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm
from articles.forms import ArticleForm

User = get_user_model()


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
        return super().render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        username = form.data['username']
        email = form.data['email']
        password = form.data['password']       
        qs = User.objects.filter(email__exact=email)
        if qs.count() == 0:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()       
        return super().form_valid(form)