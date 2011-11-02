# coding: utf-8

from django import forms
from interface.models import AsignacionCuerpoMaterialMayor, Region
from datetime import date

class FormularioAsignacionCuerpoMaterialMayor(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Región')
    
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
                    
        if 'transferencia_por_escritura_publica' in d and d['transferencia_por_escritura_publica']:
            if 'fecha_de_escritura' in d and not d['fecha_de_escritura']:
                self._errors['fecha_de_escritura'] = self.error_class([u'La fecha de escritura es obligatoria'])
                del d['fecha_de_escritura']
            if 'escritura_publica' in d and not d['escritura_publica']:
                self._errors['escritura_publica'] = self.error_class([u'El archivo de escritura es obligatorio'])
                del d['escritura_publica']
            if 'notaria' in d and not d['notaria']:
                self._errors['notaria'] = self.error_class([u'La notaria es obligatoria'])
                del d['notaria']
            if 'numero_de_repertorio' in d and not d['numero_de_repertorio']:
                self._errors['numero_de_repertorio'] = self.error_class([u'El número de repertorio es obligatorio'])
                del d['numero_de_repertorio']
                
        return d
    
    class Meta:
        model = AsignacionCuerpoMaterialMayor
        fields = ('region', 'cuerpo', 'compania', 'fecha_de_asignacion', 'acta_de_entrega_de_asignacion', 'listado_de_material_menor', 'transferencia_por_escritura_publica', 'fecha_de_escritura', 'escritura_publica', 'notaria', 'numero_de_repertorio', 'observaciones')
        widgets = {
            'fecha_de_asignacion': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_de_escritura': forms.DateInput(attrs={'class': 'datepicker'})
        }

