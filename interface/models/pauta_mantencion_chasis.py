# coding: utf-8

from django.db import models
from . import PautaMantencion

class PautaMantencionChasis(PautaMantencion):
    
    def __unicode__(self):
        return unicode(self.pautamantencion)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Pauta de Mantención de Chasis'
        verbose_name_plural = u'Pautas de Mantención de Chasis'
