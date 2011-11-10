# coding: utf-8

from django.db import models
from . import OperacionMantencion

class OperacionMantencionPauta(OperacionMantencion):
    pauta = models.ForeignKey('PautaMantencion')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']
        app_label = 'interface'
        verbose_name = u'Operación mantención pauta'
        verbose_name_plural = u'Operaciones mantención pauta'
