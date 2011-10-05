# coding: utf-8

from django import forms
from interface.models import AsignacionCuerpoMaterialMayor, Region
from datetime import date

class FormularioHojaVidaAsignacionCuerpoMaterialMayor(forms.ModelForm):
    class Meta:
        model = AsignacionCuerpoMaterialMayor
        fields = ('fecha_de_asignacion', 'fecha_de_transferencia', 'notaria', 'numero_de_repertorio', 'acta_de_entrega_de_asignacion', 'listado_de_material_menor', 'observaciones')
        widgets = {
            'fecha_de_asignacion': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_de_transferencia': forms.DateInput(attrs={'class': 'datepicker'})
        }

