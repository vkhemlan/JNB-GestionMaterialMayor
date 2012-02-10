# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.models.evento_hoja_vida_material_mayor import generate_uploaded_hoja_de_vida_file_name

class CambioDenominacion(EventoHojaVidaMaterialMayor):
    nueva_denominacion = models.CharField(max_length=255)

    def quick_details(self):
        return u'Cambio de denominación'
        
    def breadcrumb_details(self):
        return u'Cambio de denominación'
        
    def title_details(self):
        return u'Cambio de denominación'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de denominación'
        verbose_name_plural = u'Cambios de denominación'
