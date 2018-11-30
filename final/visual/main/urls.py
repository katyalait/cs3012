from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login', views.get_login, name='get_login'),
    path('your-git', views.show, name='show')
]
