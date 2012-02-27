# coding: utf-8

from django import forms
from interface.models.cambio_numero_serie_material_mayor import CambioNumeroSerieMaterialMayor

class FormularioHojaVidaCambioNumeroSerieMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroSerieMaterialMayor
        fields = ()

