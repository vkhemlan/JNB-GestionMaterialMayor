# coding: utf-8

from django import forms
from django.core.urlresolvers import reverse
from interface.models import Region, Cuerpo, MaterialMayor, Compania

class MaterialMayorSearchForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, empty_label='Nivel JNBC')
    cuerpo = forms.ModelChoiceField(queryset=Cuerpo.objects.order_by('nombre'), required=False,
        empty_label='Ver todos')
        
    def get_filtered_material_mayor(self):
        self.full_clean()
        
        material_mayor = MaterialMayor.objects.filter(validado_por_operaciones=True)
        
        d = self.data
        
        if 'region' in d and d['region'] and int(d['region']):
            material_mayor = material_mayor.filter(cuerpo__comuna__provincia__region__id=d['region'])
        else:
            material_mayor = material_mayor.filter(cuerpo__isnull=True)
            
        if 'cuerpo' in d and d['cuerpo'] and int(d['cuerpo']):
            material_mayor = material_mayor.filter(cuerpo__id=d['cuerpo'])
                
        return material_mayor
        
    def get_path(self):
        result = []
        
        d = self.data
        
        if 'region' in d and d['region'] and int(d['region']):
            result.append('region=%d' % int(d['region']))
        if 'cuerpo' in d and d['cuerpo'] and int(d['cuerpo']):
            result.append('cuerpo=%d' % int(d['cuerpo']))
            
        return '&'.join(result)
