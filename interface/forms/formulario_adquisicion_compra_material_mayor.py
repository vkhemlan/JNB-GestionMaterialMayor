# coding: utf-8

from django import forms
from interface.models import AdquisicionCompraMaterialMayor
from . import BaseModelForm

class FormularioAdquisicionCompraMaterialMayor(BaseModelForm):
    fecha_orden_de_compra = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    fecha_declaracion_de_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    def render_detalles(self):
        fields = self._field_range('orden_de_compra', 'manual_de_mantencion')
        return self._render_fields_as_list(fields)
               
    class Meta:
        model = AdquisicionCompraMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo')
