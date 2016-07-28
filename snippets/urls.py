#coding=utf-8

from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'/snippets/$', views.SnippetList.as_view()),
    url(r'/snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)