# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    url(r'^$', 'index', name='index'),
    url(r'^logout/$', 'logout', name='logout'),
    (r'^material_mayor/dar_de_alta/compra/$', 'adquisicion_compra_material_mayor'),
    (r'^material_mayor/dar_de_alta/donacion/$', 'adquisicion_donacion_material_mayor'),
    (r'^material_mayor/no_asignados/$', 'material_mayor_sin_asignar'),
    (r'^material_mayor/(?P<material_mayor_id>\d+)/$', 'editar_material_mayor'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/adquisicion/$', 'editar_adquisicion_material_mayor'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/asignar_a_cuerpo/$', 'asignar_material_mayor_a_cuerpo'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/hoja_de_vida/$', 'detalles_hoja_de_vida_material_mayor'),
    (r'material_mayor/(?P<material_mayor_id>\d+)/hoja_de_vida/(?P<evento_id>\d+)/$', 'detalle_evento_hoja_de_vida_material_mayor'),
)

urlpatterns += patterns('interface.views_services',
    (r'^services/part_model_list/$', 'part_model_list'),
)
