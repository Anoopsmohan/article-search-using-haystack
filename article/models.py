from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title