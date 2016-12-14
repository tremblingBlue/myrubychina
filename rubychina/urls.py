from django.conf.urls import url

from . import views

app_name = 'rubychina'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^articles$', views.articles, name="articles"),
    url(r'^login$', views.Login.as_view(), name="login"),
    url(r'^logout$', views.user_logout, name="logout"),
]