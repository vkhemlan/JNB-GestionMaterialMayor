# coding: utf-8

from django.db import models

class MarcaChasisMaterialMayor(models.Model):
    name = models.CharField(max_length = 255)
    ordering = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'name']
        app_label = 'interface'
        verbose_name = u'Marca de chasis de Material Mayor'
        verbose_name_plural = u'Marcas de chasis de Material Mayor'