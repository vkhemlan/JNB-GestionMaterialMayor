# coding: utf-8

from django.db import models

class ModoAdquisicionMaterialMayor(models.Model):
    name = models.CharField(max_length = 255)
    classname = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'interface'
        verbose_name = u'Modo de adquisición de Material Mayor'
        verbose_name_plural = u'Modo de adquisición de Material Mayor'