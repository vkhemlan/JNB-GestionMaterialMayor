# coding: utf-8

from django.db import models

class FamiliaUsoMaterialMayor(models.Model):
    nombre = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        app_label = 'interface'
        verbose_name = u'Familia de usos de material mayor'
        verbose_name_plural = u'Familias de usos de material mayor'
