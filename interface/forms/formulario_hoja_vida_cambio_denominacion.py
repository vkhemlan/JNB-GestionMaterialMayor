# coding: utf-8

from django import forms
from interface.models import CambioDenominacion

class FormularioHojaVidaCambioDenominacion(forms.ModelForm):
    
    class Meta:
        model = CambioDenominacion
        fields = ()

