# coding: utf-8

from django.db import models
from . import PautaMantencion

class PautaMantencionCarrosado(PautaMantencion):
    
    def __unicode__(self):
        return unicode(self.pautamantencion_ptr)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Pauta de Mantención de Carrosado'
        verbose_name_plural = u'Pautas de Mantención de Carrosado'
