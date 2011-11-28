# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class DadaDeBajaMaterialMayor(EventoHojaVidaMaterialMayor):
    motivo = models.ForeignKey('MotivoDadaDeBaja')
    observaciones = models.TextField(blank=True, null=True)
    
    def quick_details(self):
        return u'Vehículo dado de baja'
        
    def breadcrumb_details(self):
        return u'Vehículo dado de baja'
        
    def title_details(self):
        return u'Vehículo dado de baja'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Dada de baja de merial mayor'
        verbose_name_plural = u'Dadas de baja de material mayor'
