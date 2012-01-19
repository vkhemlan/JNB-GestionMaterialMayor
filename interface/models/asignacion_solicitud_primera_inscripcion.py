# coding: utf-8

from django.db import models
from . import EventoHojaVidaMaterialMayor
from interface.models.evento_hoja_vida_material_mayor import generate_uploaded_hoja_de_vida_file_name

class AsignacionSolicitudPrimeraInscripcion(EventoHojaVidaMaterialMayor):
    solicitud_primera_inscripcion = models.FileField(upload_to=lambda i, fn:  generate_uploaded_hoja_de_vida_file_name('solicitud_primera_inscripcion', i, fn), verbose_name=u'Solicitud de primera inscripcion')

    def quick_details(self):
        return u'Asignación de solicitud de primera inscripción'
        
    def breadcrumb_details(self):
        return u'Asignación de solicitud de primera inscripción'
        
    def title_details(self):
        return u'Asignación de solicitud de primera inscripción'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Asig. de solicitud de primera insc.'
        verbose_name_plural = u'Asig. de solicitud de primera insc.'
