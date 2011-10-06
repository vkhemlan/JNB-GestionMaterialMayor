# coding: utf-8

from django import forms
from interface.models import AsignacionPatenteMaterialMayor

class FormularioAsignacionPatenteMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = AsignacionPatenteMaterialMayor
        fields = ['patente']

