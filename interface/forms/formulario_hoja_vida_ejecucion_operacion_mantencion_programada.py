# coding: utf-8

from django import forms
from interface.models import EjecucionOperacionMantencionProgramada

class FormularioHojaVidaEjecucionOperacionMantencionProgramada(forms.ModelForm):
    class Meta:
        model = EjecucionOperacionMantencionProgramada
        fields = ()

