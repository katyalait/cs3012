from django.urls import path
from django.conf.urls import url
from github import Github
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('login', views.get_login, name='get_login'),
    path('your-git', views.show, name='show')
]
