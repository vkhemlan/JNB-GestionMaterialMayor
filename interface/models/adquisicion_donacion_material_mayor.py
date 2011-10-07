# coding: utf-8

from django.db import models
from . import AdquisicionMaterialMayor
from adquisicion_material_mayor import generate_uploaded_adquisicion_file_name

class AdquisicionDonacionMaterialMayor(AdquisicionMaterialMayor):
    donante = models.CharField(max_length=255, verbose_name=u'Donante', blank=True, null=True)
    factura = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('factura', i, fn), verbose_name=u'Factura (sin valor comercial)', blank=True, null=True)
    bill_of_lading = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('bill_of_lading', i, fn), verbose_name=u'Bill of Lading', blank=True, null=True)
    packing_list = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('packing_list', i, fn), verbose_name=u'Packing List', blank=True, null=True)
    declaracion_de_ingreso = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('declaracion_de_ingreso', i, fn), verbose_name=u'Declaración de Ingreso', blank=True, null=True)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición por donación'
        verbose_name_plural = u'Adquisiciones por donación'
