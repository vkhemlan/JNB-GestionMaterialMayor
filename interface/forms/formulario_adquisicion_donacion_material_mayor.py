# coding: utf-8

from django import forms
from interface.models import AdquisicionDonacionMaterialMayor, Region
from . import BaseModelForm

class FormularioAdquisicionDonacionMaterialMayor(BaseModelForm):
    region_cuerpo_destinatario = forms.ModelChoiceField(queryset=Region.objects.all())

    def render_detalles(self):
        fields = self._field_range('donante', 'declaracion_de_ingreso')
        fields.append(self['region_cuerpo_destinatario'])
        fields.append(self['cuerpo_destinatario'])
        return self._render_fields_as_list(fields)
        
    @classmethod
    def get_from_instance(self, adquisicion):
        form = self(instance=adquisicion)
        if adquisicion.cuerpo_destinatario:
            form.initial['region_cuerpo_destinatario'] = adquisicion.cuerpo_destinatario.comuna.provincia.region
        return form
               
    class Meta:
        model = AdquisicionDonacionMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo')
