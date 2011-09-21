# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    (r'^$', 'index'),
    url(r'^logout/$', 'logout', name='logout'),
)

urlpatterns += patterns('interface.views_account',
    (r'^account/refresh_base_data/$', 'refresh_base_data'),
)

urlpatterns += patterns('interface.views_staff',
    (r'^adquisicion_compra_material_mayor/$', 'adquisicion_compra_material_mayor'),
    (r'^adquisicion_donacion_material_mayor/$', 'adquisicion_donacion_material_mayor'),
    (r'material_mayor/$', 'material_mayor'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/$', 'material_mayor_details'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/adquisicion/$', 'material_mayor_adquisicion_details'),
)
