# coding: utf-8

from django import forms
from django.core.urlresolvers import reverse
from interface.models import Region, Cuerpo, MaterialMayor, Compania

class MaterialMayorSearchForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, 
        empty_label='JNBC')
    cuerpo = forms.ModelChoiceField(queryset=Cuerpo.objects.order_by('nombre'), required=False,
        empty_label='Ver todos')
        
    def get_filtered_material_mayor(self):
        self.full_clean()
        
        region = None
        if 'region' in self.data and self.data['region']:
            try:
                region = Region.objects.get(pk=self.data['region'])
            except Region.DoesNotExist:
                pass
            
        cuerpo = None
        if 'cuerpo' in self.data and self.data['cuerpo']:
            try:
                cuerpo = Cuerpo.objects.get(pk=self.data['cuerpo'])
            except Cuerpo.DoesNotExist:
                pass
            
        if not region:
            result = {
                'title': 'Material mayor a nivel JNBC',
                'potentially_has_material_mayor': True,
                'material_mayor': MaterialMayor.objects.filter(cuerpo__isnull=True),
                'children': [],
                'breadcrumbs': []
                }
        elif not cuerpo:
            children = []
            
            for cuerpo in Cuerpo.objects.filter(comuna__provincia__region=region).order_by('nombre'):
                children.append({
                    'title': unicode(cuerpo),
                    'link_url': '?region=%d&cuerpo=%d' % (cuerpo.comuna.provincia.region.id, cuerpo.id,),
                    'material_mayor': MaterialMayor.objects.filter(cuerpo=cuerpo),
                    'children': []
                })
            
            result = {
                'title': 'Material mayor de la %s' %  (unicode(region),),
                'potentially_has_material_mayor': False,
                'material_mayor': [],
                'children': children,
                'breadcrumbs': [[unicode(region), reverse('interface.views.material_mayor') + '?region=%d' % region.id]]
                }
        else:
            children = []
            
            for compania in Compania.objects.filter(cuerpo=cuerpo).order_by('numero'):
                children.append({
                    'title': unicode(compania),
                    'material_mayor': MaterialMayor.objects.filter(compania=compania),
                    'children': []
                })
            
            result = {
                'title': 'Material mayor a nivel de cuerpo',
                'potentially_has_material_mayor': True,
                'material_mayor': MaterialMayor.objects.filter(cuerpo=cuerpo, compania__isnull=True),
                'children': children,
                'breadcrumbs': [
                    [unicode(region), reverse('interface.views.material_mayor') + '?region=%d' % region.id],
                    [unicode(cuerpo), reverse('interface.views.material_mayor') + '?region=%d&cuerpo=%d' % (region.id, cuerpo.id,)]
                ]
                }
                
        return result
