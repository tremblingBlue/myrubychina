from django.conf.urls import url

from . import views
from .views import auth

app_name = 'rubychina'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^articles$', views.articles, name="articles"),
    url(r'^login$', auth.Login.as_view(), name="login"),
    url(r'^logout$', auth.user_logout, name="logout"),
    url(r'^register$', auth.Register.as_view(), name="register"),
]