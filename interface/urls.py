# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    (r'^/$', 'index'),
    url(r'^logout/$', 'logout', name='logout'),
)