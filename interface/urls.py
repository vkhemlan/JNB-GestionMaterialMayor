# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    (r'^$', 'index'),
    url(r'^logout/$', 'logout', name='logout'),
)

urlpatterns += patterns('interface.views_staff',
    (r'^adquisicion_compra_material_mayor/$', 'adquisicion_compra_material_mayor'),
    (r'^adquisicion_donacion_material_mayor/$', 'adquisicion_donacion_material_mayor'),
)