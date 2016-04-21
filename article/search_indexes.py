__author__ = 'anoop.sm'

import datetime

from haystack import indexes
from article.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    likes = indexes.IntegerField(model_attr='likes')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """
        Used when the entire index for model is updated.
        """
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
