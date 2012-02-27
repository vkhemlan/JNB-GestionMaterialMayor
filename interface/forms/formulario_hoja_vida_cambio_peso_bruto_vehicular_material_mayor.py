# coding: utf-8

from django import forms
from interface.models.cambio_peso_bruto_vehicular_material_mayor import CambioPesoBrutoVehicularMaterialMayor

class FormularioHojaVidaCambioPesoBrutoVehicularMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioPesoBrutoVehicularMaterialMayor
        fields = ()

