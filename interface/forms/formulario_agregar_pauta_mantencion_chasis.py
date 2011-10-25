# coding: utf-8

from django import forms
from interface.models import PautaMantencionChasis

class FormularioAgregarPautaMantencionChasis(forms.ModelForm):
    
    class Meta:
        model = PautaMantencionChasis
        fields = ['name']

