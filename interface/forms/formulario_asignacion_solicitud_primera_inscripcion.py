# coding: utf-8

from django import forms
from interface.models.asignacion_solicitud_primera_inscripcion import AsignacionSolicitudPrimeraInscripcion

class FormularioAsignacionSolicitudPrimeraInscripcion(forms.ModelForm):
    
    class Meta:
        model = AsignacionSolicitudPrimeraInscripcion
        fields = ['solicitud_primera_inscripcion']
