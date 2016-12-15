#!/usr/bin/env python
# coding=utf-8
__author__ = 'simplemx'

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views import View

from ..views import DEFAULT_VIEW, render


def user_logout(request):
    current_view = request.GET.get('current_view', DEFAULT_VIEW)
    logout(request)
    messages.success(request, 'Success logout')
    return redirect('rubychina:%s' % current_view)


class Login(View):
    def get(self, request, *args, **kwargs):
        next = request.GET.get('next', None)
        return render(request, 'login.html', {'next': next})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        next = request.POST.get('next', DEFAULT_VIEW)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Success login')
            return redirect('rubychina:%s' % next)
        else:
            messages.error(request, 'username or password is invalidate')
            return render(request, 'login.html', {'next': next})


class Register(View):
    def get(self, request):
        next = request.GET.get('next', None)
        return render(request, 'register.html', {'next': next})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        next = request.POST.get('next', DEFAULT_VIEW)

        if password != confirm_password:
            messages.error(request, 'password is not match to confirm password')
            return render(request, 'register.html', {'next': next})

        # check user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'register user is exists')
            return render(request, 'register.html', {'next': next})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        validate = authenticate(username=username, password=password)
        if validate is not None:
            login(request, user)
            messages.success(request, 'Success register')
            return redirect('rubychina:%s' % next)
        else:
            messages.error(request, 'login fail, please try again later')
            return render(request, 'index.html', {'next': next})
