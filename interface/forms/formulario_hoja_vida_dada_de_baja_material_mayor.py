# coding: utf-8

from django import forms
from interface.models import CambioCertificadoAnotacionesVigentes

class FormularioHojaVidaDadaDeBajaMaterialMayor(forms.ModelForm):
    class Meta:
        model = CambioCertificadoAnotacionesVigentes
        fields = ()

