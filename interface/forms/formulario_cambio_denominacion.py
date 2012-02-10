# coding: utf-8

from django import forms
from interface.models import CambioDenominacion

class FormularioCambioDenominacion(forms.ModelForm):
    
    class Meta:
        model = CambioDenominacion
        fields = ('nueva_denominacion',)

