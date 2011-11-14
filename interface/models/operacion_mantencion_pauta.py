# coding: utf-8

from django.db import models

class OperacionMantencionPauta(models.Model):
    pauta = models.ForeignKey('PautaMantencion')
    descripcion = models.TextField()
    frecuencia = models.ForeignKey('FrecuenciaOperacion')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']
        app_label = 'interface'
        verbose_name = u'Operación mantención pauta'
        verbose_name_plural = u'Operaciones mantención pauta'
