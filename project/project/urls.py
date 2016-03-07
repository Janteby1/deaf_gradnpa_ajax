from django.conf.urls import patterns, include, url
from django.contrib import admin
from deafgrandpa.views import GrandpaView

urlpatterns = patterns('',
    url(r'^home$', GrandpaView.as_view(), name='index'),
)
