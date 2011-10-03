# coding: utf-8

from django import forms
from interface.models import AdquisicionMaterialMayor, Rol, Region, Cuerpo
from . import BaseModelForm, FormularioDestinatarioAdquisicionMaterialMayor
from django.conf import settings
from django.template import loader, Context

class FormularioAdquisicionMaterialMayor(BaseModelForm):
    
    def __init__(self, *args, **kwargs):
        profile = kwargs['user'].get_profile()
        del kwargs['user']
        
        super(FormularioAdquisicionMaterialMayor, self).__init__(*args, **kwargs)

        if profile.rol == Rol.OPERACIONES() or profile.rol == Rol.ADQUISICIONES():
            self.fields['region_cuerpo_destinatario'] = forms.ModelChoiceField(queryset=Region.objects.all())
            self.fields['cuerpo_destinatario'] = forms.ModelChoiceField(queryset=Cuerpo.objects.all())
            
    def get_instance(self, user):
        adquisicion = self.instance
        adquisicion.usuario = user
        if 'cuerpo_destinatario' in self.fields:
            adquisicion.cuerpo_destinatario = self.cleaned_data['cuerpo_destinatario']
        else:
            adquisicion.cuerpo_destinatario = user.get_profile().cuerpo
        return adquisicion
        
    @classmethod
    def get_from_instance(self, adquisicion):
        form = self(instance=adquisicion)
        if adquisicion.cuerpo_destinatario:
            form.initial['region_cuerpo_destinatario'] = adquisicion.cuerpo_destinatario.comuna.provincia.region
        return form
               
    class Meta:
        model = AdquisicionMaterialMayor
