# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.models.evento_hoja_vida_material_mayor import generate_uploaded_hoja_de_vida_file_name

class AsignacionCuerpoMaterialMayor(EventoHojaVidaMaterialMayor):
    cuerpo = models.ForeignKey('Cuerpo')
    compania = models.ForeignKey('Compania', blank=True, null=True, verbose_name='Compañía')
    
    fecha_de_asignacion = models.DateField(verbose_name='Fecha de asignación', blank=True, null=True)
    notaria = models.CharField(max_length=255, blank=True, null=True)
    numero_de_repertorio = models.CharField(max_length=255, blank=True, null=True, verbose_name='N° de repertorio')
    acta_de_entrega_de_asignacion = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('acta_de_entrega_de_asignacion', i, fn), verbose_name=u'Acta de entrega de asignación', blank=True, null=True)
    listado_de_material_menor = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('listado_de_material_menor', i, fn), verbose_name=u'Listado de material menor', blank=True, null=True)
    
    transferencia_por_escritura_publica = models.BooleanField(default=False)
    fecha_de_escritura = models.DateField(blank=True, null=True)
    escritura_publica = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('escritura_publica', i, fn), verbose_name=u'Escritura pública', blank=True, null=True)
    
    observaciones = models.TextField(blank=True, null=True)
    
    def quick_details(self):
        return u'Material asignado a %s' % (unicode(self.cuerpo))
        
    def breadcrumb_details(self):
        return u'Asignación a cuerpo'
        
    def title_details(self):
        return u'Asignación a cuerpo'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Asignación a cuerpo'
        verbose_name_plural = u'Asignaciones a cuerpo'
