# coding: utf-8

from django import forms

class FormularioPautaMantencionCarrosadoAgregar(forms.Form):
    pauta_mantencion = forms.FileField(label=u'Pauta de mantención (en formato Excel)')

