# coding: utf-8

from django.conf.urls.defaults import *
from django.contrib.auth.views import login

urlpatterns = patterns('interface.views',
    (r'^$', 'index'),
)