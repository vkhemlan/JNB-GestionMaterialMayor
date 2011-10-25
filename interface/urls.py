# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('interface.views',
    url(r'^$', 'index', name='index'),
    url(r'^logout/$', 'logout', name='logout'),
    (r'^pauta_mantencion/carrosado/$', 'pauta_mantencion_carrosado'),
    (r'^pauta_mantencion/carrosado/(?P<pauta_mantencion_carrosado_id>\d+)/$', 'pauta_mantencion_carrosado_editar'),
    (r'^pauta_mantencion/carrosado/(?P<pauta_mantencion_carrosado_id>\d+)/eliminar/$', 'pauta_mantencion_carrosado_eliminar'),
    (r'^pauta_mantencion/carrosado/agregar/$', 'agregar_pauta_mantencion_carrosado'),
    (r'^pauta_mantencion/chasis/$', 'pauta_mantencion_chasis'),
    (r'^pauta_mantencion/chasis/(?P<pauta_mantencion_chasis_id>\d+)/$', 'pauta_mantencion_chasis_editar'),
    (r'^pauta_mantencion/chasis/(?P<pauta_mantencion_chasis_id>\d+)/eliminar/$', 'pauta_mantencion_chasis_eliminar'),
    (r'^pauta_mantencion/chasis/agregar/$', 'agregar_pauta_mantencion_chasis'),
    (r'^material_mayor/$', 'material_mayor'),
    (r'^material_mayor.xls$', 'material_mayor_excel'),
    (r'^material_mayor/dar_de_alta/compra/$', 'adquisicion_compra_material_mayor'),
    (r'^material_mayor/dar_de_alta/donacion/$', 'adquisicion_donacion_material_mayor'),
    (r'^material_mayor/sin_asignar/$', 'material_mayor_sin_asignar'),
    (r'^material_mayor/sin_asignar.xls$', 'material_mayor_sin_asignar_excel'),
    (r'^material_mayor/(?P<material_mayor>\d+)/$', 'editar_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/cambiar_pauta_mantencion_carrosado/$', 'cambiar_pauta_mantencion_carrosado'),
    (r'material_mayor/(?P<material_mayor>\d+)/validar/$', 'validar_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/adquisicion/$', 'editar_adquisicion_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/asignar_a_cuerpo/$', 'asignar_material_mayor_a_cuerpo'),
    (r'material_mayor/(?P<material_mayor>\d+)/asignar_a_compania/$', 'asignar_material_mayor_a_compania'),
    (r'material_mayor/(?P<material_mayor>\d+)/asignar_patente/$', 'asignar_patente_a_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/detalles_patente/$', 'detalles_patente_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/hoja_de_vida/$', 'detalles_hoja_de_vida_material_mayor'),
    (r'material_mayor/(?P<material_mayor>\d+)/hoja_de_vida/(?P<evento_id>\d+)/$', 'detalle_evento_hoja_de_vida_material_mayor'),
)

urlpatterns += patterns('interface.views_media',
    (r'media/documentos/material_mayor/(?P<material_mayor>\d+)/(?P<field_name>\w+)\.(?P<extension>\w+)$','descargar_documento_material_mayor'),
    (r'media/fotografias/material_mayor/(?P<material_mayor>\d+)/(?P<field_name>\w+)\.(?P<extension>\w+)$','descargar_fotografia_material_mayor'),
    (r'media/documentos/material_mayor/(?P<material_mayor>\d+)/adquisicion/(?P<field_name>\w+)\.(?P<extension>\w+)$','descargar_documento_adquisicion_material_mayor'),
    (r'media/documentos/material_mayor/(?P<material_mayor>\d+)/evento_hoja_vida/(?P<evento_id>\d+)-(?P<field_name>\w+)\.(?P<extension>\w+)$','descargar_documento_evento_material_mayor'),
)

urlpatterns += patterns('interface.views_services',
    (r'^services/part_model_list/$', 'part_model_list'),
)
