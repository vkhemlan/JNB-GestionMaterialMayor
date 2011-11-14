# coding: utf-8

from django import forms
from interface.models import ArchivoMantencionProgramada

class FormularioAgregarArchivoMantencionProgramada(forms.ModelForm):
    
    class Meta:
        model = ArchivoMantencionProgramada
        fields = ('nombre', 'archivo')

