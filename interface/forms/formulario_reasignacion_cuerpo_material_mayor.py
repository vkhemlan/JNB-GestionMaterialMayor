# coding: utf-8

from django import forms
from interface.models import ReasignacionCuerpoMaterialMayor, Region

class FormularioReasignacionCuerpoMaterialMayor(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    
    class Meta:
        model = ReasignacionCuerpoMaterialMayor
        fields = ('region', 'cuerpo',)
    
    
    

