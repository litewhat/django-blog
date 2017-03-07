from django import forms

from accounts.models import UserProfile


class UserProfileForm(forms.ModelForm):
    house = forms.CharField()
    apartment = forms.CharField()

    class Meta:
        model = UserProfile
        exclude = ['user']
