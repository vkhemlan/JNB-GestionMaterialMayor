# coding: utf-8

from django.db import models

class FrecuenciaOperacion(models.Model):
    numero_meses = models.IntegerField()
    
    def __unicode__(self):
        return '%d meses' % self.numero_meses

    class Meta:
        ordering = ['numero_meses']
        app_label = 'interface'
        verbose_name = u'Frecuencia de operación'
        verbose_name_plural = u'Frecuencias de operación'
