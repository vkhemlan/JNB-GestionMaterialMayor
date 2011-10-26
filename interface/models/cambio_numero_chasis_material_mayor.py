# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioNumeroChasisMaterialMayor(EventoHojaVidaMaterialMayor):
    nuevo_numero_chasis = models.CharField(max_length=255, verbose_name=u'Nuevo número de chasis')
    
    def quick_details(self):
        return u'Cambio de número de chasis a %s' % self.nuevo_numero_chasis
        
    def breadcrumb_details(self):
        return u'Cambio de número de chasis'
        
    def title_details(self):
        return u'Cambio de número de chasis'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de número de chasis'
        verbose_name_plural = u'Cambios de número de chasis'
