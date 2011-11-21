# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class AsignacionPatenteMaterialMayor(EventoHojaVidaMaterialMayor):
    patente = models.CharField(max_length = 6, help_text=u'Formato: ABCD12')
    digito_verificador = models.CharField(max_length=1, blank=True, null=True, help_text=u'Un caracter, se puede dejar en blanco')
    
    def __unicode__(self):
        result = self.patente
        if self.digito_verificador:
            result = result + '-' + self.digito_verificador
        return result
        
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
