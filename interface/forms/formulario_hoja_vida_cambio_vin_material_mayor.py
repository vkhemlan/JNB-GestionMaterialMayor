# coding: utf-8

from django import forms
from interface.models.cambio_vin_material_mayor import CambioVinMaterialMayor

class FormularioHojaVidaCambioVinMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioVinMaterialMayor
        fields = ()

