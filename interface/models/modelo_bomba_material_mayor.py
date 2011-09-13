# coding: utf-8

from django.db import models

class ModeloBombaMaterialMayor(models.Model):
    marca = models.ForeignKey('MarcaBombaMaterialMayor')
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return '%s %s' % (unicode(self.marca), self.name)

    class Meta:
        ordering = ['marca', 'name']
        app_label = 'interface'
        verbose_name = u'Modelo de bomba de Material Mayor'
        verbose_name_plural = u'Modelo de bomba de Material Mayor'
