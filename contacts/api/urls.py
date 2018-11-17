
from django.conf.urls import url
from django.contrib import admin

from .views import (
    PhonebookCreateAPIView,
    PhonebookDeleteAPIView,
    PhonebookDetailAPIView,
    PhonebookListAPIView,
    PhonebookUpdateAPIView
    )

urlpatterns = [
    url(r'^$', PhonebookListAPIView.as_view(), name='list'),
    url(r'^create/$', PhonebookCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/$', PhonebookDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\w-]+)/edit/$', PhonebookUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', PhonebookDeleteAPIView.as_view(), name='delete'),
]
