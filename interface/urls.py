# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    (r'^$', 'index'),
    url(r'^logout/$', 'logout', name='logout'),
)

urlpatterns += patterns('interface.views_staff',
    (r'^dar_de_alta_material_mayor/$', 'dar_de_alta_material_mayor'),
)