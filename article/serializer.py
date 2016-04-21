__author__ = 'anoop.sm'
from django.contrib.auth.models import User

from rest_framework import serializers
from article.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ('url', 'author', 'pub_date', 'title', 'body', 'likes')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'articles')


class SearchSerializer(serializers.Serializer):
    #author = serializers.ReadOnlyField(source='author.username')

    url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    author = serializers.CharField()
    pub_date = serializers.DateTimeField()
    title = serializers.CharField()
    body = serializers.CharField()
    likes = serializers.IntegerField()


