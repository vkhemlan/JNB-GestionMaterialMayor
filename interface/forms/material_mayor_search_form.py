# coding: utf-8

from django import forms
from interface.models import Region, Cuerpo, MaterialMayor

class MaterialMayorSearchForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, empty_label='Nivel JNBC')
    cuerpo = forms.ModelChoiceField(queryset=Cuerpo.objects.order_by('nombre'), required=False,
        empty_label='Ver todos')
    incluir_dados_de_baja = forms.BooleanField(required=False)
        
    def get_filtered_material_mayor(self):
        self.full_clean()
        
        data = self.data

        material_mayor = MaterialMayor.objects.filter(validado_por_operaciones=True)

        if not 'incluir_dados_de_baja' in data or not data['incluir_dados_de_baja']:
            material_mayor = MaterialMayor.objects.filter(dada_de_baja__isnull=True)
        
        if 'region' in data and data['region'] and int(data['region']):
            material_mayor = material_mayor.filter(cuerpo__comuna__provincia__region__id=data['region'])
        else:
            material_mayor = material_mayor.filter(cuerpo__isnull=True)
            
        if 'cuerpo' in data and data['cuerpo'] and int(data['cuerpo']):
            material_mayor = material_mayor.filter(cuerpo__id=data['cuerpo'])

                
        return material_mayor
        
    def get_path(self):
        result = []
        
        d = self.data
        
        if 'region' in d and d['region'] and int(d['region']):
            result.append('region=%d' % int(d['region']))
        if 'cuerpo' in d and d['cuerpo'] and int(d['cuerpo']):
            result.append('cuerpo=%d' % int(d['cuerpo']))
            
        return '&'.join(result)
