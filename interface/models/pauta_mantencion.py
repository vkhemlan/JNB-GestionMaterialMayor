# coding: utf-8

from django.db import models

class PautaMantencion(models.Model):
    name = models.CharField(max_length = 255, verbose_name='Nombre')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'interface'
        verbose_name = u'Pauta de Mantención'
        verbose_name_plural = u'Pautas de Mantención'
