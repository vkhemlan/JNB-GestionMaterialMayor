# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioNumeroSerieMaterialMayor(EventoHojaVidaMaterialMayor):
    nuevo_numero_serie = models.CharField(max_length=255, verbose_name=u'Nuevo número de serie')
    
    def quick_details(self):
        return u'Cambio de número de serie a %s' % self.nuevo_numero_serie
        
    def breadcrumb_details(self):
        return u'Cambio de número de serie'
        
    def title_details(self):
        return u'Cambio de número de serie'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de número de serie'
        verbose_name_plural = u'Cambios de número de serie'
