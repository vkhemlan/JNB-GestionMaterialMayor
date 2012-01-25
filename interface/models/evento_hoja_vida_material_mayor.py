# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from interface.models.tipo_evento_hoja_vida_material_mayor import TipoEventoHojaVidaMaterialMayor

def generate_uploaded_hoja_de_vida_file_name(field_name, evento, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'documentos/material_mayor/%d/evento_hoja_vida/%d-%s.%s' % (evento.material_mayor.id, evento.id, field_name, extension)

class EventoHojaVidaMaterialMayor(models.Model):
    material_mayor = models.ForeignKey('MaterialMayor')
    usuario = models.ForeignKey(User)
    cargos_usuario = models.ManyToManyField('Cargo', blank=True, null=True)
    rol_usuario = models.ForeignKey('Rol', blank=True, null=True)
    cuerpo_usuario = models.ForeignKey('Cuerpo', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey('TipoEventoHojaVidaMaterialMayor')
    
    def __unicode__(self):
        return unicode(self.tipo)
        
    def get_polymorphic_instance(self):
        if self.__class__.__name__ != 'EventoHojaVidaMaterialMayor':
            return self
        else:
            my_models = __import__('interface.models', fromlist=['interface'])
            BaseClass = getattr(my_models, self.tipo.classname)
            return BaseClass.objects.get(pk=self.id)

    def cargar_informacion_hoja_de_vida(self, material_mayor, user, classname):
        self.material_mayor = material_mayor
        self.usuario = user
        self.rol_usuario = user.get_profile().rol
        self.tipo = TipoEventoHojaVidaMaterialMayor.objects.get(classname=classname)
        self.save()
        for cargo in user.get_profile().cargos.all():
            self.cargos_usuario.add(cargo)
        self.cuerpo_usuario = user.get_profile().cuerpo
        self.save()

    class Meta:
        ordering = ['material_mayor', 'fecha']
        app_label = 'interface'
        verbose_name = u'Evento hoja de vida'
        verbose_name_plural = u'Eventos hoja de vida'
