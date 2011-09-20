# coding: utf-8

from django.db import models
from . import MaterialMayor

class AdquisicionMaterialMayor(models.Model):
    modo = models.ForeignKey('ModoAdquisicionMaterialMayor')

    def __unicode__(self):
        try:
            return u'Adquisición de %s' % (unicode(self.materialmayor,))
        except MaterialMayor.DoesNotExist:
            return u'Adquisición no asignada'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición de Material Mayor'
        verbose_name_plural = u'Adquisiciones de Material Mayor'
