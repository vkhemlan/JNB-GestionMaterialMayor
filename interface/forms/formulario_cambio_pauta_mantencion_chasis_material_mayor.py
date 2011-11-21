# coding: utf-8

from django import forms
from interface.models.modelo_chasis_material_mayor import ModeloChasisMaterialMayor

class FormularioCambioPautaMantencionChasisMaterialMayor(forms.ModelForm):

    class Meta:
        model = ModeloChasisMaterialMayor
        fields = ('pauta_mantencion',)
