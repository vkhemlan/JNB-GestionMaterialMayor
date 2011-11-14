# coding: utf-8

from django import forms
from interface.models import AdquisicionDonacionMaterialMayor, Region
from . import FormularioAdquisicionMaterialMayor

class FormularioAdquisicionDonacionMaterialMayor(FormularioAdquisicionMaterialMayor):

    def render_detalles(self):
        fields = self._field_range('donante', 'declaracion_de_ingreso')
        if 'region_cuerpo_destinatario' in self.fields:
            fields.append(self['region_cuerpo_destinatario'])
            fields.append(self['cuerpo_destinatario'])
        return self._render_fields_as_list(fields)

    def clean(self):
        d = self.cleaned_data
        if 'forma_adquisicion' in d and d['forma_adquisicion'] == 'Comodato':
            if not 'dueno_comodato' in d or not d['dueno_comodato']:
                self._errors['dueno_comodato'] = self.error_class(['Este campo es obligatorio'])
                del d['dueno_comodato']

        return d
               
    class Meta:
        model = AdquisicionDonacionMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo', 'cuerpo_destinatario')
        widgets = {
            'fecha_vencimiento_limitacion_dominio': forms.DateInput(attrs={'class': 'datepicker'}),
        }
