# coding: utf-8

from django.db import models
from interface.models.material_mayor import MaterialMayor
from interface.models.operacion_mantencion_programada import OperacionMantencionProgramada

class MantencionProgramada(models.Model):
    material_mayor = models.ForeignKey('MaterialMayor')
    fecha = models.DateField()

    def __unicode__(self):
        return '%s - %s' % (unicode(self.material_mayor), unicode(self.fecha),)

    def gestor_string(self):
        return 'Mantenimiento de %s' % unicode(self.fecha)

    @classmethod
    def get_pendientes(cls, cuerpo=None):
        material_mayor = MaterialMayor.vehiculos_en_alta()
        if cuerpo:
            material_mayor = material_mayor.filter(cuerpo=cuerpo)

        operaciones_mantencion_pendientes = OperacionMantencionProgramada.objects.filter(mantencion__material_mayor__in = material_mayor, ejecucion__isnull=True)
        return set([oper.mantencion for oper in operaciones_mantencion_pendientes])

    class Meta:
        app_label = 'interface'
        verbose_name = u'Mantención programada'
        verbose_name_plural = u'Mantenciones programadas'
