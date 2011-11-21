# coding: utf-8

from django import forms
from interface.models import AsignacionCompaniaMaterialMayor, Compania

class FormularioAsignacionCompaniaMaterialMayor(forms.ModelForm):

    def __init__(self, material_mayor, *args, **kwargs):
        super(FormularioAsignacionCompaniaMaterialMayor, self).__init__(*args, **kwargs)
        self.fields['compania'].queryset = Compania.objects.filter(cuerpo=material_mayor.cuerpo)
    
    class Meta:
        model = AsignacionCompaniaMaterialMayor
        fields = ('compania', 'numero_orden_del_dia', 'fecha_orden_del_dia', 'orden_del_dia')
        widgets = {
            'fecha_orden_del_dia': forms.DateInput(attrs={'class': 'datepicker'}),
        }

