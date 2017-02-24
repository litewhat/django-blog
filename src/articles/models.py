from django.db import models
from django.urls import reverse

from accounts.models import UserProfile


class Article(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{} | {}'.format(self.title, self.updated)

    def comments(self):
        return self.comment_set.all().order_by('-created')

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.id})

    def author(self):
        return self.user_profile.user.username


class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'article: {} | {}'.format(self.article.id, self.created)

    def author(self):
        return self.user_profile.user.username

