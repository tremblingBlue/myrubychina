#!/usr/bin/env python
# coding=utf-8
__author__ = 'simplemx'

from django.shortcuts import render as _render
from django.core.urlresolvers import resolve

from ..models import Node, Article


DEFAULT_VIEW = 'index'


def render(request, template, context):
    """Add global attribute"""
    context = {} if context is None else context
    context['current_view'] = resolve(request.path_info).url_name
    return _render(request, template, context)


def index(request):
    node_list = Node.objects.order_by('-create_date')[:10]
    article_list = Article.objects.order_by('-create_date')[:20]
    context = {
        'user': request.user,
        'latest_nodes': node_list,
        'latest_articles': article_list
    }
    return render(request, 'index.html', context)


def articles(request):
    article_list = Article.objects.order_by('-create_date')[:50]
    return render(request, 'articles.html', {'articles': article_list})

