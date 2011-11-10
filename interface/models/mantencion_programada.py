# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor

class MantencionProgramada(models.Model):
    material_mayor = models.ForeignKey('MaterialMayor')
    fecha = models.DateField()

    def __unicode__(self):
        return '%s - %s' % (unicode(self.material_mayor), unicode(self.fecha),)

    def gestor_string(self):
        return 'Mantenimiento de %s' % unicode(self.fecha)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Mantención programada'
        verbose_name_plural = u'Mantenciones programadas'
