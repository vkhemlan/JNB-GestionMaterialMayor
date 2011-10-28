# coding: utf-8

from django import forms

class FormularioPautaMantencionChasisAgregar(forms.Form):
    pauta_mantencion = forms.FileField(label=u'Pauta de mantención (en formato Excel)')

