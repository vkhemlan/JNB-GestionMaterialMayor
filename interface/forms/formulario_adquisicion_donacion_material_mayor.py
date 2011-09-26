# coding: utf-8

from django import forms
from interface.models import AdquisicionDonacionMaterialMayor
from . import BaseModelForm

class FormularioAdquisicionDonacionMaterialMayor(BaseModelForm):

    def render_detalles(self):
        fields = self._field_range('donante', 'declaracion_de_ingreso')
        return self._render_fields_as_list(fields)
               
    class Meta:
        model = AdquisicionDonacionMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo')
