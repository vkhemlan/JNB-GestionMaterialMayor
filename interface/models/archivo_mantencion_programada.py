# coding: utf-8

from django.db import models

def generate_uploaded_archivo_mantencion_programada_file_name(instance, filename):
    left_path, extension = filename.rsplit('.',1)

    return 'documentos/material_mayor/%d/mantenciones_programadas/%d/%d.%s' % (instance.mantencion.material_mayor.id, instance.mantencion.id, instance.id, extension)

class ArchivoMantencionProgramada(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    archivo = models.FileField(upload_to=lambda i, fn:  generate_uploaded_archivo_mantencion_programada_file_name(i, fn), verbose_name='Archivo', blank=True, null=True)
    mantencion = models.ForeignKey('MantencionProgramada')

    def __unicode__(self):
        return unicode(self.nombre)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Archivo de mantención programada'
        verbose_name_plural = u'Archivos de mantención programada'
