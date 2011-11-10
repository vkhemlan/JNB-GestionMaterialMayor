# coding: utf-8

from django.db import models
from . import OperacionMantencion

class OperacionMantencionProgramada(OperacionMantencion):
    mantencion = models.ForeignKey('MantencionProgramada')
    ejecucion = models.OneToOneField('EjecucionOperacionMantencionProgramada', blank=True, null=True)
    
    def __unicode__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']
        app_label = 'interface'
        verbose_name = u'Operación mantención programada'
        verbose_name_plural = u'Operaciones mantención programadas'
