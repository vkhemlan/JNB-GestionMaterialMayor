# coding: utf-8

from django import forms
from interface.models import AdquisicionCompraMaterialMayor
from . import FormularioAdquisicionMaterialMayor
from django.conf import settings
from django.template import loader, Context

class FormularioAdquisicionCompraMaterialMayor(FormularioAdquisicionMaterialMayor):
    """
    Clase que representa el Formulario para dar de alta un vehículo vía compra
    """

    fecha_orden_de_compra = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)
    fecha_declaracion_de_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), required=False)
    
    def render_detalles(self):
        """
        Método que genera la parte del formulario de dar de alta un material mayor asociada a su adquisición por compra.
        """
        template = loader.get_template('formularios/adquisicion_material_mayor_compra.html')

        c = Context({
            'form': self,
            'STATIC_URL': settings.STATIC_URL
        })

        return template.render(c)

    def render_subdetalles(self):
        """
        Método llamado por el template "adquisicion_material_mayor_compra" (ver método render_detalles) para generar
        iterativamente los campos lineales el formulario como HTML.
        """
        fields = self._field_range('factura_comercial', 'manual_de_mantencion')
        if 'region_cuerpo_destinatario' in self.fields:
            fields.append(self['region_cuerpo_destinatario'])
            fields.append(self['cuerpo_destinatario'])

        return self._render_fields_as_list(fields, blacklist=['region_cuerpo_destinatario', 'cuerpo_destinatario'])
               
    class Meta:
        model = AdquisicionCompraMaterialMayor
        exclude = ('modo_adquisicion', 'usuario', 'fecha', 'modo')