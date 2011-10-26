# coding: utf-8

from django import forms
from interface.models import MaterialMayor, MarcaChasisMaterialMayor, MarcaCarrosadoMaterialMayor, MarcaCajaCambioMaterialMayor, MarcaBombaMaterialMayor, PautaMantencionCarrosado
from . import BaseModelForm

class FormularioEditarMaterialMayor(BaseModelForm):
    marca_caja_cambio = forms.ModelChoiceField(queryset=MarcaCajaCambioMaterialMayor.objects.all(), required=False)
    marca_bomba = forms.ModelChoiceField(queryset=MarcaBombaMaterialMayor.objects.all(), required=False)
    
    def __init__(self, *args, **kwargs):
        profile = kwargs['user'].get_profile()
        
        super(FormularioEditarMaterialMayor, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        
        if 'uso' in data and data['uso'] and data['uso'].is_others_option:
            if 'otro_uso' in data and not data['otro_uso']:
                self._errors['otro_uso'] = self.error_class([u'Este campo es obligatorio'])
                del data['otro_uso']
        
        validation_pairs = [
            ['caja_cambio', 'de la caja de cambio'],
            ['bomba', 'de la bomba']]
        
        for part_type, message in validation_pairs:
            marca_string = 'marca_%s' % (part_type,)
            modelo_string = 'modelo_%s' % (part_type,)
            
            if marca_string in data and modelo_string in data and data[modelo_string] and data[modelo_string].marca != data[marca_string]:
                self._errors[modelo_string] = self.error_class([u'La marca %s debe coincidir con su modelo' % message])
                del data[modelo_string]

        return data

    def render_datos_vehiculo(self):
        fields = self._field_range('tipo_vehiculo', 'color')
        return self._render_fields_as_list(fields)
        
    def render_informacion_adicional(self):
        fields = self._field_range('condicion', 'planos')
        fields.insert(2, self['marca_caja_cambio'])
        fields.insert(5, self['marca_bomba'])
        return self._render_fields_as_list(fields)

    def picture_fields(self):
        fields = self._field_range('fotografia_frontal', 'fotografia_trasera')
        return [(field, getattr(self.instance, field.name)) for field in fields]
        
    @classmethod
    def get_from_instance(self, instance, user):
        form = FormularioEditarMaterialMayor(instance=instance, user=user)
        if instance.modelo_caja_cambio:
            form.initial['marca_caja_cambio'] = instance.modelo_caja_cambio.marca.id
        if instance.modelo_bomba:
            form.initial['marca_bomba'] = instance.modelo_bomba.marca.id
        return form
               
    class Meta:
        model = MaterialMayor
        exclude = ('adquisicion', 'asignacion_de_patente', 'pauta_mantencion_carrosado', 'validado_por_operaciones', 'modelo_chasis', 'marca_carrosado', 'numero_chasis', 'numero_motor')
