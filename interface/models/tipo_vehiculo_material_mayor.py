# coding: utf-8

from django.db import models

class TipoVehiculoMaterialMayor(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'interface'
        verbose_name = u'Tipo de vehículo'
        verbose_name_plural = u'Tipos de vehículo'
