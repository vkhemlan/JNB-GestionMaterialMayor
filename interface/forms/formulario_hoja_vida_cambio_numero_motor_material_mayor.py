# coding: utf-8

from django import forms
from interface.models import CambioNumeroMotorMaterialMayor

class FormularioHojaVidaCambioNumeroMotorMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroMotorMaterialMayor
        fields = ()

