# coding: utf-8

from django import forms
from interface.models import Region, Cuerpo
from django.conf import settings
from django.template import loader, Context

class FormularioDestinatarioAdquisicionMaterialMayor(forms.Form):
    region_cuerpo_destinatario = forms.ModelChoiceField(queryset=Region.objects.all())
    cuerpo_destinatario = forms.ModelChoiceField(queryset=Cuerpo.objects.all())
    
    def clean(self):
        d = self.cleaned_data
        if 'region_cuerpo_destinatario' in d and 'cuerpo_destinatario' in d:
            region = d['region_cuerpo_destinatario']
            cuerpo = d['cuerpo_destinatario']
            if cuerpo.comuna.provincia.region != region:
                self._errors['cuerpo_destinatario'] = self.error_class([u'El cuerpo debe pertenecer a la región'])
                del d['cuerpo_destinatario']
                
        return d
                
