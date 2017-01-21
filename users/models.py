from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='photo', null=True, blank=True)
