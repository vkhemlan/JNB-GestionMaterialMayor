# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class EventoHojaVidaMaterialMayor(models.Model):
    material_mayor = models.ForeignKey('MaterialMayor')
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey('TipoEventoHojaVidaMaterialMayor')
    
    def __unicode__(self):
        return unicode(self.tipo)
        
    def get_polymorphic_instance(self):
        from . import ReasignacionCuerpoMaterialMayor
        if self.__class__.__name__ != 'EventoHojaVidaMaterialMayor':
            return self
        else:
            BaseClass = eval(self.tipo.classname)
            return BaseClass.objects.get(pk=self.id)

    class Meta:
        ordering = ['material_mayor', 'fecha']
        app_label = 'interface'
        verbose_name = u'Evento hoja de vida'
        verbose_name_plural = u'Eventos hoja de vida'
