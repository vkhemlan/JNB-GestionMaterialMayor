# coding: utf-8

from django import forms
from interface.models import DadaDeBajaMaterialMayor

class FormularioDarDeBajaMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = DadaDeBajaMaterialMayor
        fields = ['motivo', 'observaciones']
