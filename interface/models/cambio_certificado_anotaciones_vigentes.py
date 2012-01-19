# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.models.evento_hoja_vida_material_mayor import generate_uploaded_hoja_de_vida_file_name

class CambioCertificadoAnotacionesVigentes(EventoHojaVidaMaterialMayor):
    certificado_anotaciones_vigentes = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('certificado_anotaciones_vigentes', i, fn), verbose_name=u'Nuevo certificado de anotaciones vigentes')

    def quick_details(self):
        return u'Cambio de certificado de anotaciones vigentes'
        
    def breadcrumb_details(self):
        return u'Cambio de certificado de anotaciones vigentes'
        
    def title_details(self):
        return u'Cambio de certificado de anotaciones vigentes'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Cambio de certif. de anot. vigentes'
        verbose_name_plural = u'Cambios de certif. de anot. vigentes'
