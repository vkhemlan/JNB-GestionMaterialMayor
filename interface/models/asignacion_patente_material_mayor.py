# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class AsignacionPatenteMaterialMayor(EventoHojaVidaMaterialMayor):
    patente = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.patente
        
    def quick_details(self):
        return u'Asignación de patente'
        
    def breadcrumb_details(self):
        return u'Asignación de patente'
        
    def title_details(self):
        return u'Asignación de patente'

    class Meta:
        ordering = ['patente']
        app_label = 'interface'
        verbose_name = u'Asignación de patente'
        verbose_name_plural = u'Asignaciones de patente'
