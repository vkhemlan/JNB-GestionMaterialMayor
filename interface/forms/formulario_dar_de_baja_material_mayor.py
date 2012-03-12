# coding: utf-8

from django import forms
from interface.models import DadaDeBajaMaterialMayor

class FormularioDarDeBajaMaterialMayor(forms.ModelForm):

    def clean(self):
        d = self.cleaned_data

        if d['motivo'].nombre == 'Otro' and not d['otro_motivo']:
            self._errors['otro_motivo'] = self.error_class(['Por favor especifique un motivo'])

            del d['otro_motivo']

        return d
    
    class Meta:
        model = DadaDeBajaMaterialMayor
        fields = ['fecha_dada_de_baja', 'motivo', 'otro_motivo', 'numero_orden_del_dia', 'fecha_orden_del_dia', 'archivo_orden_del_dia', 'observaciones']
        widgets = {
            'fecha_dada_de_baja': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_orden_del_dia': forms.DateInput(attrs={'class': 'datepicker'})
        }