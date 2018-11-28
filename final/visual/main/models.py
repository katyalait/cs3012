from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repo = models.CharField(max_length=120)

    def __str__(self):
        return self.username
