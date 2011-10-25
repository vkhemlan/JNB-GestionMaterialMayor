# coding: utf-8

from django import forms
from interface.models import CambioPautaMantencionCarrosadoMaterialMayor

class FormularioCambioPautaMantencionCarrosadoMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = CambioPautaMantencionCarrosadoMaterialMayor
        fields = ('nueva_pauta_mantencion_carrosado',)

