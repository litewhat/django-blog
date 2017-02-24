from django.conf.urls import url, include

from accounts.apps import AccountsConfig
from accounts.views import *

app_name = AccountsConfig.name

urlpatterns = [
	url(r'^(?P<username>\w+)/$', ProfileHomeView.as_view(), name='profile'),
]