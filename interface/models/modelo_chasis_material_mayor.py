# coding: utf-8

from django.db import models

class ModeloChasisMaterialMayor(models.Model):
    marca = models.ForeignKey('MarcaChasisMaterialMayor')
    name = models.CharField(max_length = 255)
    pauta_mantencion = models.ForeignKey('PautaMantencionChasis')
    
    def __unicode__(self):
        return self.name

    def full_name(self):
        return '%s %s' % (unicode(self.marca), self.name)

    class Meta:
        ordering = ['marca', 'name']
        app_label = 'interface'
        verbose_name = u'Modelo de chasis'
        verbose_name_plural = u'Modelos de chasis'
