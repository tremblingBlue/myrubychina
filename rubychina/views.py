from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import Node, Article
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


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
    logout(request)
    return HttpResponseRedirect(reverse('rubychina:index'))

class Login(View):
    
    def get(self, request, *args, **kwargs):
        next = request.GET['next']
        return render(request, 'login.html', {'next': next})
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next:
                return HttpResponseRedirect(reverse('rubychina:%s' % next))
            else:
                return HttpResponseRedirect(reverse('rubychina:index'))
        else:
            return render(request, 'login.html', {'error':'username/password is invalidate', 'next': next})
