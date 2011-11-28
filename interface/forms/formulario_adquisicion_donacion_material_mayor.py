# coding: utf-8

from django import forms
from interface.models import AdquisicionDonacionMaterialMayor
from . import FormularioAdquisicionMaterialMayor

class FormularioAdquisicionDonacionMaterialMayor(FormularioAdquisicionMaterialMayor):
    """
    Clase que representa la parte de adquisición del formulario para dar de alta un vehículo a través de una donación o
    comodato
    """

    def render_detalles(self):
        """
        Método que genera el formulario como HTML considerando el cargo del usuario usado en el constructor
        """
        fields = self._field_range('donante', 'declaracion_de_ingreso')
        if 'region_cuerpo_destinatario' in self.fields:
            fields.append(self['region_cuerpo_destinatario'])
            fields.append(self['cuerpo_destinatario'])
        return self._render_fields_as_list(fields)

    def clean(self):
        """
        Redefinimos el método clean del formulario para verificar que, en el caso de una adquisición por comodato,
        se especifique el dueño del mismo. En el caso de una donación este campo no es obligatorio por lo que hay
        que verificarlo manualmente.
        """
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
