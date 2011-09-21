# coding: utf-8

from django import forms
from interface.models import MaterialMayor, MarcaChasisMaterialMayor, MarcaCarrosadoMaterialMayor, MarcaCajaCambioMaterialMayor, MarcaBombaMaterialMayor
from . import BaseModelForm

class FormularioDarDeAltaMaterialMayor(BaseModelForm):
    marca_chasis = forms.ModelChoiceField(queryset=MarcaChasisMaterialMayor.objects.all())
    marca_carrosado = forms.ModelChoiceField(queryset=MarcaCarrosadoMaterialMayor.objects.all())
    marca_caja_cambio = forms.ModelChoiceField(queryset=MarcaCajaCambioMaterialMayor.objects.all())
    marca_bomba = forms.ModelChoiceField(queryset=MarcaBombaMaterialMayor.objects.all())

    def clean(self):
        data = self.cleaned_data
        
        validation_pairs = [
            ['chasis', 'del chasis'], 
            ['carrosado', 'del carrosado'],
            ['caja_cambio', 'de la caja de cambio'],
            ['bomba', 'de la bomba']]
        
        for part_type, message in validation_pairs:
            marca_string = 'marca_%s' % (part_type,)
            modelo_string = 'modelo_%s' % (part_type,)
            
            if marca_string in data and modelo_string in data and data[modelo_string].marca != data[marca_string]:
                self._errors[modelo_string] = self.error_class([u'La marca %s debe coincidir con su modelo' % message])
                del data[modelo_string]

        if hasattr(self, 'custom_clean'):
            data = self.custom_clean()

        return data

    def render_datos_vehiculo(self):
        fields = self._field_range('tipo_vehiculo', 'placa_patente')
        fields.insert(1, self['marca_chasis'])
        return self._render_fields_as_list(fields)
        
    def render_informacion_adicional(self):
        fields = self._field_range('modelo_carrosado', 'pais_origen')
        fields.insert(0, self['marca_carrosado'])
        fields.insert(3, self['marca_caja_cambio'])
        fields.insert(7, self['marca_bomba'])
        return self._render_fields_as_list(fields) 

    def picture_fields(self):
        fields = self._field_range('fotografia_frontal', 'fotografia_trasera')
        return [(field, getattr(self.instance, field.name)) for field in fields]
        
    @classmethod
    def get_from_instance(self, instance):
        form = FormularioDarDeAltaMaterialMayor(instance=instance)
        form.initial['marca_chasis'] = instance.modelo_chasis.marca.id
        form.initial['marca_carrosado'] = instance.modelo_carrosado.marca.id
        form.initial['marca_caja_cambio'] = instance.modelo_caja_cambio.marca.id
        form.initial['marca_bomba'] = instance.modelo_bomba.marca.id
        return form
               
    class Meta:
        model = MaterialMayor
        exclude = ('adquisicion',)
