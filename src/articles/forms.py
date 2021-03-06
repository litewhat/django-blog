from django.forms import ModelForm

from articles.models import Article

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ['user_profile', 'liked_by', 'created', 'updated']