# coding: utf-8

from django.db import models

class TipoVehiculoMaterialMayor(models.Model):
    name = models.CharField(max_length = 255)
    ordering = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'name']
        app_label = 'interface'
        verbose_name = u'Tipo de Vehículo de Material Mayor'
        verbose_name_plural = u'Tipos de Vehículo de Material Mayor'