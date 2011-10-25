# coding: utf-8

from django.db import models

class OperacionMantencion(models.Model):
    pauta = models.ForeignKey('PautaMantencion')
    descripcion = models.CharField(max_length=255)
    frecuencia = models.ForeignKey('FrecuenciaOperacion')
    
    def __unicode__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']
        app_label = 'interface'
        verbose_name = u'Operación'
        verbose_name_plural = u'Operaciones'
