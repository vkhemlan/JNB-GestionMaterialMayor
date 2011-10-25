# coding: utf-8

from django import forms
from interface.models import PautaMantencionCarrosado

class FormularioAgregarPautaMantencionCarrosado(forms.ModelForm):
    
    class Meta:
        model = PautaMantencionCarrosado
        fields = ['name']

