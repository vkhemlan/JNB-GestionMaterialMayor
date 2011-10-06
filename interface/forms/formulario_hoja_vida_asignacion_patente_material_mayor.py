# coding: utf-8

from django import forms
from interface.models import AsignacionPatenteMaterialMayor
from datetime import date

class FormularioHojaVidaAsignacionPatenteMaterialMayor(forms.ModelForm):
    class Meta:
        model = AsignacionPatenteMaterialMayor
        fields = ()

