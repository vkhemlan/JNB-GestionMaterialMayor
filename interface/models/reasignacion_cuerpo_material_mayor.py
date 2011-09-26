# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class ReasignacionCuerpoMaterialMayor(EventoHojaVidaMaterialMayor):
    cuerpo = models.ForeignKey('cuerpo')
    
    def quick_details(self):
        return u'Material reasignado al %s' % (unicode(self.cuerpo))
        
    def breadcrumb_details(self):
        return u'Reasignación de cuerpo'
        
    def title_details(self):
        return u'Reasignación de cuerpo'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Reasignación a cuerpo'
        verbose_name_plural = u'Reasignaciones a cuerpo'
