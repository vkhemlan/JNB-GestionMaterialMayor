# coding: utf-8

from django import forms
from interface.models import CambioCertificadoAnotacionesVigentes

class FormularioHojaVidaCambioCertificadoAnotacionesVigentes(forms.ModelForm):
    class Meta:
        model = CambioCertificadoAnotacionesVigentes
        fields = ()

