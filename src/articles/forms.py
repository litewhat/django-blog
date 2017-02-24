from django.forms import ModelForm

from .models import Article

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ['user_profile', 'created', 'updated']