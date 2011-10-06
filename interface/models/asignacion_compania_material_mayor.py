# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.utils import generate_uploaded_hoja_de_vida_file_name

class AsignacionCompaniaMaterialMayor(EventoHojaVidaMaterialMayor):
    compania = models.ForeignKey('Compania', verbose_name='Compañía')
        
    def quick_details(self):
        return u'Material asignado a %s' % (unicode(self.compania))
        
    def breadcrumb_details(self):
        return u'Asignación a compañía'
        
    def title_details(self):
        return u'Asignación a compañía'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Asignación a compañía'
        verbose_name_plural = u'Asignaciones a compañías'
