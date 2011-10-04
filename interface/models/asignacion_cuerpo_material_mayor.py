# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class AsignacionCuerpoMaterialMayor(EventoHojaVidaMaterialMayor):
    cuerpo = models.ForeignKey('Cuerpo')
    compania = models.ForeignKey('Compania', blank=True, null=True, verbose_name='Compañía')
    fecha_de_asignacion = models.DateField()
    acta_de_entrega_de_asignacion = models.FileField(upload_to='actas_de_entrega_de_asignacion', verbose_name=u'Acta de entrega de asignación')
    listado_de_material_menor = models.FileField(upload_to='listados_de_material_menor', verbose_name=u'Listado de material menor')
    observaciones = models.TextField(blank=True, null=True)
    
    def quick_details(self):
        return u'Material asignado al %s' % (unicode(self.cuerpo))
        
    def breadcrumb_details(self):
        return u'Asignación de cuerpo'
        
    def title_details(self):
        return u'Asignación de cuerpo'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Asignación a cuerpo'
        verbose_name_plural = u'Asignaciones a cuerpo'
