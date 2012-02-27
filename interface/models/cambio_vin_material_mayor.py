# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioVinMaterialMayor(EventoHojaVidaMaterialMayor):
    nuevo_vin = models.CharField(max_length=255, verbose_name=u'Nuevo VIN')
    
    def quick_details(self):
        return u'Cambio de VIN a %s' % self.nuevo_vin
        
    def breadcrumb_details(self):
        return u'Cambio de VIN'
        
    def title_details(self):
        return u'Cambio de VIN'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de VIN'
        verbose_name_plural = u'Cambios de VIN'
