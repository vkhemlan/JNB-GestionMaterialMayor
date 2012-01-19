# coding: utf-8

from django import forms
from interface.models import DadaDeBajaMaterialMayor

class FormularioDarDeBajaMaterialMayor(forms.ModelForm):
    
    class Meta:
        model = DadaDeBajaMaterialMayor
        fields = ['fecha_dada_de_baja', 'motivo', 'numero_orden_del_dia', 'fecha_orden_del_dia', 'archivo_orden_del_dia', 'observaciones']
        widgets = {
            'fecha_dada_de_baja': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_orden_del_dia': forms.DateInput(attrs={'class': 'datepicker'})
        }