# coding: utf-8

from django import forms
from interface.models import AsignacionCompaniaMaterialMayor
from datetime import date

class FormularioHojaVidaAsignacionCompaniaMaterialMayor(forms.ModelForm):
    class Meta:
        model = AsignacionCompaniaMaterialMayor
        fields = ()

