# coding: utf-8

from django.db import models

class UsoMaterialMayor(models.Model):
    nombre = models.CharField(max_length = 255)
    familia = models.ForeignKey('FamiliaUsoMaterialMayor')
    
    def __unicode__(self):
        return '%s - %s' % (unicode(self.familia), self.nombre)

    class Meta:
        ordering = ['familia', 'nombre']
        app_label = 'interface'
        verbose_name = u'Uso de material mayor'
        verbose_name_plural = u'Usos de material mayor'
