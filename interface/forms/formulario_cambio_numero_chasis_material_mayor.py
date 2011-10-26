# coding: utf-8

from django import forms
from interface.models import CambioNumeroChasisMaterialMayor

class FormularioCambioNumeroChasisMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroChasisMaterialMayor
        fields = ('nuevo_numero_chasis',)

