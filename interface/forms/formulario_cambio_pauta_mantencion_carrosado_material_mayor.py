# coding: utf-8

from django import forms
from interface.models import PautaMantencionCarrosado

class FormularioCambioPautaMantencionCarrosadoMaterialMayor(forms.Form):
    pauta_mantencion_carrosado = forms.ModelChoiceField(queryset=PautaMantencionCarrosado.objects.all())
