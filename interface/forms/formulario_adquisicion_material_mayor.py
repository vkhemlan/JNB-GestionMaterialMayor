# coding: utf-8

from django import forms
from interface.models import AdquisicionMaterialMayor, Region, Cuerpo
from . import BaseModelForm

class FormularioAdquisicionMaterialMayor(BaseModelForm):
    """
    Clase base para los formularios para dar de alta material mayor
    """
    cuerpo_destinatario = forms.ModelChoiceField(queryset=Cuerpo.objects.all())
    
    def __init__(self, *args, **kwargs):
        """
        El constructor es redefinido para ver si agregamos dinámicamente algunos campos si es que los permisos del
        usuario lo ameritan
        """
        profile = kwargs['user'].get_profile()
        
        super(FormularioAdquisicionMaterialMayor, self).__init__(*args, **kwargs)

        if profile.is_staff_jnbc():
            self.fields['region_cuerpo_destinatario'] = forms.ModelChoiceField(queryset=Region.objects.all(), label='Región del cuerpo destinatario')
            self.fields['cuerpo_destinatario'] = forms.ModelChoiceField(queryset=Cuerpo.objects.all(), label='Cuerpo de bomberos destinatario')
            
    def get_instance(self, user):
        """
        Método que retorna la instancia asociada al formulario
        Podríamos usar la variable de instancia "instance" de ModelForm, pero hay que considerar que se debe verificar
        la existencia del campo dinámico que se pudo haber agregado en el constructor.
        """
        adquisicion = self.instance
        adquisicion.usuario = user
        if 'cuerpo_destinatario' in self.fields:
            adquisicion.cuerpo_destinatario = self.cleaned_data['cuerpo_destinatario']
        else:
            adquisicion.cuerpo_destinatario = user.get_profile().cuerpo
        return adquisicion
        
    @classmethod
    def get_from_instance(cls, adquisicion, user):
        """
        Método que, a partir de una instancia de adquisicion de material mayor, genera un formulario de esta clase
        Nuevamente podríamos haber usado el constructor de ModelForm pero también era necesario considerar la
        inicialización de los campos dinámicos del formulario.
        """
        form = cls(instance=adquisicion, user=user)
        if adquisicion.cuerpo_destinatario:
            form.initial['region_cuerpo_destinatario'] = adquisicion.cuerpo_destinatario.comuna.provincia.region
        return form
               
    class Meta:
        model = AdquisicionMaterialMayor
