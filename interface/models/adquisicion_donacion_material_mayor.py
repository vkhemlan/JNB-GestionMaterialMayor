# coding: utf-8

from django.db import models
from . import AdquisicionMaterialMayor

class AdquisicionDonacionMaterialMayor(AdquisicionMaterialMayor):
    donante = models.CharField(max_length=255, verbose_name=u'Donante')
    factura = models.FileField(upload_to='facturas_donaciones', verbose_name=u'Factura (sin valor comercial)', blank=True, null=True)
    bill_of_lading = models.FileField(upload_to='bills_of_lading_donaciones', verbose_name=u'Bill of Lading', blank=True, null=True)
    packing_list = models.FileField(upload_to='packing_lists_donaciones', verbose_name=u'Packing List', blank=True, null=True)
    declaracion_de_ingreso = models.FileField(upload_to='declaraciones_de_ingreso_donaciones', verbose_name=u'Declaración de Ingreso', blank=True, null=True)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición por donación'
        verbose_name_plural = u'Adquisiciones por donación'
