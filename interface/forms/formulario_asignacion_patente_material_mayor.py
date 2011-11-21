# coding: utf-8

from django import forms
from interface.models import AsignacionPatenteMaterialMayor
import re

class FormularioAsignacionPatenteMaterialMayor(forms.ModelForm):

    def clean_patente(self):
        data = self.cleaned_data['patente']
        patente_regular_expression = r'^[A-Z]{2}([0-9]{2})|([A-Z]{2})[0-9]{2}$'
        if not re.search(patente_regular_expression, data):
            raise forms.ValidationError(u'Por favor ingrese una patente en formato "AB1234" o "ABCD12", recuerde el uso de mayúsculas')

        return data

    def clean_digito_verificador(self):
        data = self.cleaned_data['digito_verificador']
        if not data:
            return None
        valid_range = [str(i) for i in range(10)]
        valid_range.append('K')
        if data not in valid_range:
            raise forms.ValidationError(u'El dígito verificador debe estar entre 0 y 9 o ser "K" mayúscula')

        return data
    
    class Meta:
        model = AsignacionPatenteMaterialMayor
        fields = ['patente', 'digito_verificador']

