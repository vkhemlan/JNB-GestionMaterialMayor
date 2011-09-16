# coding: utf-8

from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        app_label = 'interface'
        verbose_name = u'País'
        verbose_name_plural = u'Paises'
