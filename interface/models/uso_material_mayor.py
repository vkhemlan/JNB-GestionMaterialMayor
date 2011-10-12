# coding: utf-8

from django.db import models

class UsoMaterialMayor(models.Model):
    nombre = models.CharField(max_length = 255)
    familia = models.ForeignKey('FamiliaUsoMaterialMayor')
    is_others_option = models.BooleanField(default=False)
    
    def __unicode__(self):
        if self.is_others_option or not self.nombre.strip():
            return unicode(self.familia)
        else:
            return '%s %s' % (unicode(self.familia), self.nombre)

    class Meta:
        ordering = ['familia', 'nombre']
        app_label = 'interface'
        verbose_name = u'Uso de material mayor'
        verbose_name_plural = u'Usos de material mayor'
