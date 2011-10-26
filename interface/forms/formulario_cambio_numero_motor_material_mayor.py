# coding: utf-8

from django import forms
from interface.models import CambioNumeroMotorMaterialMayor

class FormularioCambioNumeroMotorMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroMotorMaterialMayor
        fields = ('nuevo_numero_motor',)

