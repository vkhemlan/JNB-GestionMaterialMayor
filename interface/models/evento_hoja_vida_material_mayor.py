# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

def generate_uploaded_hoja_de_vida_file_name(field_name, evento, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'documentos/material_mayor/%d/evento_hoja_vida/%d-%s.%s' % (evento.material_mayor.id, evento.id, field_name, extension)

class EventoHojaVidaMaterialMayor(models.Model):
    material_mayor = models.ForeignKey('MaterialMayor')
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey('TipoEventoHojaVidaMaterialMayor')
    
    def __unicode__(self):
        return unicode(self.tipo)
        
    def get_polymorphic_instance(self):
        from . import AsignacionCuerpoMaterialMayor, AsignacionCompaniaMaterialMayor, AsignacionPatenteMaterialMayor, CambioPautaMantencionCarrosadoMaterialMayor
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
