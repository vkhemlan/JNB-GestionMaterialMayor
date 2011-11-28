# coding: utf-8

from django.db import models

class MotivoDadaDeBaja(models.Model):
    nombre = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        app_label = 'interface'
        verbose_name = u'Motivo de dada de baja'
        verbose_name_plural = u'Motivos de dada de baja'
