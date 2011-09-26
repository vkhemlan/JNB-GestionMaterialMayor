# coding: utf-8

from django.db import models

class TipoEventoHojaVidaMaterialMayor(models.Model):
    name = models.CharField(max_length=255)
    classname = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'interface'
        verbose_name = u'Tipo evento hoja de vida'
        verbose_name_plural = u'Tipos evento hoja de vida'
