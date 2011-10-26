# coding: utf-8

from django import forms
from interface.models import MaterialMayor, MarcaChasisMaterialMayor, MarcaCarrosadoMaterialMayor, MarcaCajaCambioMaterialMayor, MarcaBombaMaterialMayor, PautaMantencionCarrosado
from . import BaseModelForm

class FormularioAgregarMaterialMayor(BaseModelForm):
    marca_chasis = forms.ModelChoiceField(queryset=MarcaChasisMaterialMayor.objects.all())
    marca_caja_cambio = forms.ModelChoiceField(queryset=MarcaCajaCambioMaterialMayor.objects.all(), required=False)
    marca_bomba = forms.ModelChoiceField(queryset=MarcaBombaMaterialMayor.objects.all(), required=False)
    
    def __init__(self, *args, **kwargs):
        profile = kwargs['user'].get_profile()
        
        super(FormularioAgregarMaterialMayor, self).__init__(*args, **kwargs)

        if profile.is_staff_jnbc():
            self.fields['pauta_mantencion_carrosado'] = forms.ModelChoiceField(queryset=PautaMantencionCarrosado.objects.all(), label='Pauta de mantención del carrosado')

    def clean(self):
        data = self.cleaned_data
        
        if 'uso' in data and data['uso'] and data['uso'].is_others_option:
            if 'otro_uso' in data and not data['otro_uso']:
                self._errors['otro_uso'] = self.error_class([u'Este campo es obligatorio'])
                del data['otro_uso']
        
        validation_pairs = [
            ['chasis', 'del chasis'],
            ['caja_cambio', 'de la caja de cambio'],
            ['bomba', 'de la bomba']]
        
        for part_type, message in validation_pairs:
            marca_string = 'marca_%s' % (part_type,)
            modelo_string = 'modelo_%s' % (part_type,)
            
            if marca_string in data and modelo_string in data and data[modelo_string] and data[modelo_string].marca != data[marca_string]:
                self._errors[modelo_string] = self.error_class([u'La marca %s debe coincidir con su modelo' % message])
                del data[modelo_string]

        if hasattr(self, 'custom_clean'):
            data = self.custom_clean()

        return data

    def render_datos_vehiculo(self):
        fields = self._field_range('tipo_vehiculo', 'color')
        fields.insert(3, self['marca_chasis'])
        return self._render_fields_as_list(fields)
        
    def render_informacion_adicional(self):
        fields = self._field_range('marca_carrosado', 'planos')
        try:
            fields.insert(1, self['pauta_mantencion_carrosado']) 
        except KeyError:
            pass
        fields.insert(3, self['marca_caja_cambio'])
        fields.insert(6, self['marca_bomba'])
        return self._render_fields_as_list(fields, blacklist=['pauta_mantencion_carrosado'])

    def picture_fields(self):
        fields = self._field_range('fotografia_frontal', 'fotografia_trasera')
        return [(field, getattr(self.instance, field.name)) for field in fields]
        
    def get_instance(self):
        instance = self.instance
        if 'pauta_mantencion_carrosado' in self.fields:
            instance.pauta_mantencion_carrosado = self.cleaned_data['pauta_mantencion_carrosado']
            
        instance.validado_por_operaciones = True
        return instance
               
    class Meta:
        model = MaterialMayor
        exclude = ('adquisicion', 'asignacion_de_patente', 'pauta_mantencion_carrosado')
