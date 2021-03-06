"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from blog.views import *

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^register/', UserRegisterView.as_view(), name='register'),
    url(r'^search/', SearchView.as_view(), name='search'),
    url(r'^admin/', admin.site.urls),
    url(r'^livechat/', include('livechat.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^profile/', include('accounts.urls')),
    url(r'^api/articles/', include('articles.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
