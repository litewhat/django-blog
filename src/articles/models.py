from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # id = models.AutoField(primary_key=True) // django creates it automatically

    def __str__(self):
        str_repr = '{} | {}'.format(self.title, self.updated)
        return str_repr

    def comments(self):
        return self.comment_set.all().order_by('-created')

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.id})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        str_repr = 'article: {} | {}'.format(self.article.id, self.created)
        return str_repr

