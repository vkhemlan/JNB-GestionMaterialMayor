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
    (r'material_mayor/(?P<material_mayor_id>\d+)/reasignacion_cuerpo/$', 'reasignar_material_mayor_a_cuerpo'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/hoja_vida/$', 'hoja_vida_material_mayor'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/hoja_vida/(?P<evento_id>\d+)/$', 'detalle_evento_hoja_vida_material_mayor'),
)
