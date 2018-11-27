from django.urls import path

from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.get_login, name='get_login'),
]
