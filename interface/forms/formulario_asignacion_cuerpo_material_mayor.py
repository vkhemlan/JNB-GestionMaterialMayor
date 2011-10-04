# coding: utf-8

from django import forms
from interface.models import AsignacionCuerpoMaterialMayor, Region
from datetime import date

class FormularioAsignacionCuerpoMaterialMayor(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Región')
    fecha_de_asignacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), label=u'Fecha de asignación')
    
    def clean(self):
        d = self.cleaned_data
        if 'cuerpo' in d and 'region' in d:
            cuerpo = d['cuerpo']
            region = d['region']
            
            if cuerpo.comuna.provincia.region != region:
                self._errors['cuerpo'] = self.error_class([u'El cuerpo debe pertenecer a la región'])
                del d['cuerpo']
            
            if 'compania' in d and d['compania']:
                compania = d['compania']
                if compania.cuerpo != cuerpo:
                    self._errors['compania'] = self.error_class([u'La compañía debe pertenecer al cuerpo'])
                    del d['compania']
                
        return d
    
    @classmethod
    def initialize_from_material_mayor(self, material_mayor):
        default_cuerpo = material_mayor.adquisicion.cuerpo_destinatario
        default_compania_id = None
        
        if material_mayor.cuerpo:
            default_cuerpo = material_mayor.cuerpo
            
        if material_mayor.compania:
            default_compania_id = material_mayor.compania.id
        
        initial = {
            'region': default_cuerpo.comuna.provincia.region.id,
            'cuerpo': default_cuerpo.id,
            'compania': default_compania_id,
            'fecha_de_asignacion': date.today(),
            'acta_de_entrega_de_asignacion': 'adf',
        }
        
        form = self(initial)
        return form
    
    class Meta:
        model = AsignacionCuerpoMaterialMayor
        fields = ('region', 'cuerpo', 'compania', 'fecha_de_asignacion', 'acta_de_entrega_de_asignacion', 'listado_de_material_menor', 'observaciones')

