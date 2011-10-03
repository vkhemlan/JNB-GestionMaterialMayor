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
               
    class Meta:
        model = AdquisicionDonacionMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo', 'cuerpo_destinatario')
