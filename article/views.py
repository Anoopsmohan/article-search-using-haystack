from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from article.permission import IsOwnerOrReadOnly
from serializer import UserSerializer, ArticleSerializer, SearchSerializer
from article.models import Article


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SearchSerializer

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = EmptySearchQuerySet()

        if request.GET.get('q'):
            query = request.GET.get('q')
            queryset = SearchQuerySet().auto_query(query)

        return queryset



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `User list` and `User detail` actions.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)