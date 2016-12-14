from django.shortcuts import render as _render, redirect
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Node, Article


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
    context = {
        'articles': article_list
    }
    return render(request, 'articles.html', context)


def user_logout(request):
    current_view = request.GET['current_view']
    current_view = 'index' if current_view is None else current_view
    logout(request)
    messages.success(request, 'Success logout')
    return redirect('rubychina:%s' % current_view)


class Login(View):
    def get(self, request, *args, **kwargs):
        next = request.GET['next']
        return render(request, 'login.html', {'next': next})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        assert username is not None
        assert password is not None

        next = request.POST['next']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Success login')
            if next:
                return redirect('rubychina:%s' % next)
            else:
                return redirect('rubychina:index')
        else:
            return render(request, 'login.html', {'error': 'username/password is invalidate', 'next': next})
