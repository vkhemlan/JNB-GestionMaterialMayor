# coding: utf-8

from django.db import models

class MarcaBombaMaterialMayor(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'interface'
        verbose_name = u'Marca de bomba'
        verbose_name_plural = u'Marcas de bomba'
