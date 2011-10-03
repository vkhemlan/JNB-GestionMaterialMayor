# coding: utf-8

from django.db import models

class Cargo(models.Model):
    webservice_id = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        app_label = 'interface'
        verbose_name = u'Cargo'
        verbose_name_plural = u'Cargos'
