from django.urls import path

from . import views

from django.conf.urls import url, include
urlpatterns = [
    url(r'^fillDetails/$', views.fillDetails),
]
