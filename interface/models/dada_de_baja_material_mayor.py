# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

def generate_uploaded_dada_de_baja_file_name(field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)

    return 'documentos/material_mayor/%d/dada_de_baja/%s.%s' % (instance.materialmayor.id, field_name, extension)

class DadaDeBajaMaterialMayor(EventoHojaVidaMaterialMayor):
    fecha_dada_de_baja = models.DateField(verbose_name=u'Fecha')
    motivo = models.ForeignKey('MotivoDadaDeBaja')
    numero_orden_del_dia = models.CharField(max_length=255, verbose_name=u'Número orden del día')
    fecha_orden_del_dia = models.DateField(verbose_name=u'Fecha orden del día')
    archivo_orden_del_dia = models.FileField(upload_to=lambda i, fn: generate_uploaded_dada_de_baja_file_name('archivo_orden_del_dia', i, fn), verbose_name=u'Archivo orden del día')
    observaciones = models.TextField(blank=True, null=True)
    
    def quick_details(self):
        return u'Vehículo dado de baja'
        
    def breadcrumb_details(self):
        return u'Vehículo dado de baja'
        
    def title_details(self):
        return u'Vehículo dado de baja'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Baja de merial mayor'
        verbose_name_plural = u'Bajas de material mayor'
