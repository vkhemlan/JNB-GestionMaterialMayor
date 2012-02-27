# coding: utf-8

from django import forms
from interface.models.cambio_numero_serie_material_mayor import CambioNumeroSerieMaterialMayor

class FormularioCambioNumeroSerieMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroSerieMaterialMayor
        fields = ('nuevo_numero_serie',)

