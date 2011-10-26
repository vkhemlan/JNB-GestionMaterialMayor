# coding: utf-8

from django import forms
from interface.models import CambioNumeroChasisMaterialMayor

class FormularioHojaVidaCambioNumeroChasisMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioNumeroChasisMaterialMayor
        fields = ()

