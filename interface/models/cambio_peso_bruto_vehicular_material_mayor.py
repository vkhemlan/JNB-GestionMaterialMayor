# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioPesoBrutoVehicularMaterialMayor(EventoHojaVidaMaterialMayor):
    nuevo_peso_bruto_vehicular = models.PositiveIntegerField(verbose_name=u'Nuevo peso bruto vehicular')
    
    def quick_details(self):
        return u'Cambio de peso bruto vehicular a %d' % self.nuevo_peso_bruto_vehicular
        
    def breadcrumb_details(self):
        return u'Cambio de peso bruto vehicular'
        
    def title_details(self):
        return u'Cambio de peso bruto vehicular'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de peso bruto vehicular'
        verbose_name_plural = u'Cambios de peso bruto vehicular'
