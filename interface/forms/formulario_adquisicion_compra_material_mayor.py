# coding: utf-8

from django import forms
from interface.models import AdquisicionCompraMaterialMayor, Region
from . import BaseModelForm
from django.conf import settings
from django.template import loader, Context

class FormularioAdquisicionCompraMaterialMayor(BaseModelForm):
    fecha_orden_de_compra = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)
    fecha_declaracion_de_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)
    region_cuerpo_destinatario = forms.ModelChoiceField(queryset=Region.objects.all())
    
    def render_detalles(self):
        template = loader.get_template('formularios/adquisicion_material_mayor_compra.html')

        c = Context({
            'form': self,
            'STATIC_URL': settings.STATIC_URL
        })

        return template.render(c)

    def render_subdetalles(self):
        fields = self._field_range('factura_comercial', 'manual_de_mantencion')
        fields.append(self['region_cuerpo_destinatario'])
        fields.append(self['cuerpo_destinatario'])
        return self._render_fields_as_list(fields, blacklist=['region_cuerpo_destinatario', 'cuerpo_destinatario'])
        
    @classmethod
    def get_from_instance(self, adquisicion):
        form = self(instance=adquisicion)
        if adquisicion.cuerpo_destinatario:
            form.initial['region_cuerpo_destinatario'] = adquisicion.cuerpo_destinatario.comuna.provincia.region
        return form
               
    class Meta:
        model = AdquisicionCompraMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo')
