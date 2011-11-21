# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.models.evento_hoja_vida_material_mayor import generate_uploaded_hoja_de_vida_file_name

class AsignacionCompaniaMaterialMayor(EventoHojaVidaMaterialMayor):
    compania = models.ForeignKey('Compania', verbose_name='Compañía (*)')
    numero_orden_del_dia = models.CharField(max_length=255, verbose_name=u'Número de orden del día (*)')
    fecha_orden_del_dia = models.DateField(verbose_name=u'Fecha de orden del día (*)')
    orden_del_dia = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('orden_del_dia', i, fn), verbose_name=u'Orden del día', blank=True, null=True)
        
    def quick_details(self):
        return u'Material asignado a %s' % (unicode(self.compania))
        
    def breadcrumb_details(self):
        return u'Asignación a compañía'
        
    def title_details(self):
        return u'Asignación a compañía'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Asignación a compañía'
        verbose_name_plural = u'Asignaciones a compañías'
