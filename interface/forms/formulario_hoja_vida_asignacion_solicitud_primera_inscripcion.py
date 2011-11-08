# coding: utf-8

from django import forms
from interface.models import AsignacionSolicitudPrimeraInscripcion

class FormularioHojaVidaAsignacionSolicitudPrimeraInscripcion(forms.ModelForm):
    class Meta:
        model = AsignacionSolicitudPrimeraInscripcion
        fields = ()

