# coding: utf-8

from django import forms
from interface.models import MaterialMayor, MarcaChasisMaterialMayor, MarcaCarrosadoMaterialMayor, MarcaCajaCambioMaterialMayor, MarcaBombaMaterialMayor
from . import BaseModelForm

class FormularioDarDeAltaMaterialMayor(BaseModelForm):

    def render_datos_vehiculo(self):
        fields = self._field_range('tipo_vehiculo', 'color')
        return self._render_fields_as_list(fields)
        
    def render_informacion_adicional(self):
        fields = self._field_range('modelo_carrosado', 'pais_origen')
        return self._render_fields_as_list(fields) 

    def picture_fields(self):
        fields = self._field_range('fotografia_frontal', 'fotografia_trasera')
        return [(field, getattr(self.instance, field.name)) for field in fields]
        
    @classmethod
    def get_from_instance(self, instance):
        form = FormularioDarDeAltaMaterialMayor(instance=instance)
        return form
               
    class Meta:
        model = MaterialMayor
        exclude = ('adquisicion',)
