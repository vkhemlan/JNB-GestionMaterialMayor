# coding: utf-8

from django.db import models
from . import MaterialMayor
from django.contrib.auth.models import User
import os
from django.conf import settings

def generate_uploaded_adquisicion_file_name(field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)
    
    filename = 'documentos/material_mayor/%d/adquisicion/%s.%s' % (instance.materialmayor.id, field_name, extension)
    
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, filename))
    except OSError:
        pass
    
    return filename


class AdquisicionMaterialMayor(models.Model):
    modo = models.ForeignKey('ModoAdquisicionMaterialMayor')
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)
    cuerpo_destinatario = models.ForeignKey('Cuerpo')
    
    def save(self, *args, **kwargs):
        from . import ModoAdquisicionMaterialMayor
        if not self.id:
            self.modo = ModoAdquisicionMaterialMayor.objects.get(classname=self.__class__.__name__)
        super(AdquisicionMaterialMayor, self).save(*args, **kwargs)
        
    def get_polymorphic_instance(self):
        from . import AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor
        if self.__class__.__name__ != 'AdquisicionMaterialMayor':
            return self
        else:
            BaseClass = eval(self.modo.classname)
            return BaseClass.objects.get(pk=self.id)

    def __unicode__(self):
        try:
            return u'Adquisición de %s' % (unicode(self.materialmayor,))
        except MaterialMayor.DoesNotExist:
            return u'Adquisición no asignada'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición de Material Mayor'
        verbose_name_plural = u'Adquisiciones de Material Mayor'
