# coding: utf-8

from django.db import models

class ModeloBombaMaterialMayor(models.Model):
    marca = models.ForeignKey('MarcaBombaMaterialMayor')
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['marca', 'name']
        app_label = 'interface'
        verbose_name = u'Modelo de bomba'
        verbose_name_plural = u'Modelos de bomba'
