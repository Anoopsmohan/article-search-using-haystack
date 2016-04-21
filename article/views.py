from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.http import HttpResponse


def search(request):
    q = request.GET.get('q')
    articles = SearchQuerySet().auto_query(q)

    print articles[0].text

    return HttpResponse([articles[0].text])