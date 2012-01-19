# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class CambioPautaMantencionCarrosadoMaterialMayor(EventoHojaVidaMaterialMayor):
    nueva_pauta_mantencion_carrosado = models.CharField(max_length=255)
    
    def quick_details(self):
        return u'Cambio de pauta de mantención de carrosado a %s' % unicode(self.nueva_pauta_mantencion_carrosado)
        
    def breadcrumb_details(self):
        return u'Cambio de pauta de mantención de carrosado'
        
    def title_details(self):
        return u'Cambio de pauta de mantención de carrosado'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio pauta mantención carrosado'
        verbose_name_plural = u'Cambios pauta mantención carrosado'
