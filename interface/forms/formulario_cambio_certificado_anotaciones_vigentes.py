# coding: utf-8

from django import forms
from interface.models.cambio_certificado_anotaciones_vigentes import CambioCertificadoAnotacionesVigentes

class FormularioCambioCertificadoAnotacionesVigentes(forms.ModelForm):
    
    class Meta:
        model = CambioCertificadoAnotacionesVigentes
        fields = ['certificado_anotaciones_vigentes']
