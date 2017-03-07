from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts import utils


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                related_name='user_profile')
    avatar = models.ImageField(null=True)
    country = models.CharField(max_length=50, choices=utils.choices)
    state = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=20) 
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    house = models.IntegerField()
    apartment = models.IntegerField()

    def __str__(self):
        return '{}_profile'.format(self.user.username)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, **kwargs):
    user = kwargs['instance']
    if type(user) == get_user_model():
        qs = UserProfile.objects.filter(user=user)
        if qs.count() == 0:
            profile = UserProfile(user=user)
            profile.save()
