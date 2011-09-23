# coding: utf-8

from django.db import models

class ModeloCarrosadoMaterialMayor(models.Model):
    marca = models.ForeignKey('MarcaCarrosadoMaterialMayor')
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return '%s %s' % (unicode(self.marca), self.name)

    class Meta:
        ordering = ['marca', 'name']
        app_label = 'interface'
        verbose_name = u'Modelo de carrosado'
        verbose_name_plural = u'Modelos de carrosado'
