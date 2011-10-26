# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioNumeroMotorMaterialMayor(EventoHojaVidaMaterialMayor):
    nuevo_numero_motor = models.CharField(max_length=255, verbose_name=u'Nuevo número de motor')
    
    def quick_details(self):
        return u'Cambio de número de motor a %s' % self.nuevo_numero_motor
        
    def breadcrumb_details(self):
        return u'Cambio de número de motor'
        
    def title_details(self):
        return u'Cambio de número de motor'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de número de motor'
        verbose_name_plural = u'Cambios de número de motor'
