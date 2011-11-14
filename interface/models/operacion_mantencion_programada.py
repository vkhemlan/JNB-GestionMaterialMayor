# coding: utf-8

from django.db import models

class OperacionMantencionProgramada(models.Model):
    mantencion = models.ForeignKey('MantencionProgramada')
    descripcion = models.TextField()
    ejecucion = models.OneToOneField('EjecucionOperacionMantencionProgramada', blank=True, null=True)
    id_operacion_mantencion_pauta = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def esta_pendiente(self):
        return self.ejecucion == None and self.observaciones == None

    def esta_pospuesta(self):
        return self.ejecucion == None and self.observaciones != None

    def esta_ejecutada(self):
        return self.ejecucion != None
    
    def __unicode__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']
        app_label = 'interface'
        verbose_name = u'Operación mantención programada'
        verbose_name_plural = u'Operaciones mantención programadas'
