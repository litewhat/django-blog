from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '{}_profile'.format(self.user.username)


def user_post_save(sender, **kwargs):
    user = kwargs['instance']
    if type(user) == get_user_model():
        qs = UserProfile.objects.filter(user=user)
        
        if qs.count() == 0:
            profile = UserProfile(user=user)
            profile.save()


post_save.connect(user_post_save, sender=settings.AUTH_USER_MODEL)