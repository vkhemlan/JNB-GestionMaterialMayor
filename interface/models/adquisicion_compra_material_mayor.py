# coding: utf-8

from django.db import models
from . import AdquisicionMaterialMayor
from adquisicion_material_mayor import generate_uploaded_adquisicion_file_name

class AdquisicionCompraMaterialMayor(AdquisicionMaterialMayor):
    orden_de_compra = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('orden_de_compra', i, fn), verbose_name=u'Orden de compra', blank=True, null=True)
    numero_orden_de_compra = models.CharField(max_length=255, verbose_name=u'N° de orden de compra', blank=True, null=True)
    fecha_orden_de_compra = models.DateField(verbose_name=u'Fecha de orden de compra', blank=True, null=True)
    declaracion_de_ingreso = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('declaracion_de_ingreso', i, fn), verbose_name=u'Declaración de Ingreso', blank=True, null=True)
    numero_declaracion_de_ingreso = models.CharField(max_length=255, verbose_name=u'N° de declaración de ingreso', blank=True, null=True)
    fecha_declaracion_de_ingreso = models.DateField(verbose_name=u'Fecha de declaración de ingreso', blank=True, null=True)
    
    factura_comercial = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('factura_comercial', i, fn), verbose_name=u'Factura Comercial', blank=True, null=True)
    bill_of_lading = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('bill_of_lading', i, fn), verbose_name=u'Bill of Lading', blank=True, null=True)
    packing_list = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('packing_list', i, fn), verbose_name=u'Packing List', blank=True, null=True)
    acta_de_recepcion = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('acta_de_recepcion', i, fn), verbose_name=u'Acta de recepción', blank=True, null=True)
    solicitud_exencion_de_iva = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('solicitud_exencion_de_iva', i, fn), verbose_name=u'Solicitud de exención de IVA', blank=True, null=True)
    respuesta_solicitud_exencion_de_iva = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('respuesta_solicitud_exencion_de_iva', i, fn), verbose_name=u'Resolución exención de IVA', blank=True, null=True)
    valor_final_de_compra = models.IntegerField(verbose_name=u'Valor final de la compra', blank=True, null=True) 
    proveedor = models.CharField(max_length=255, verbose_name=u'Proveedor', blank=True, null=True)
    agente_de_aduana = models.CharField(max_length=255, verbose_name=u'Agente de aduana', blank=True, null=True)
    manual_de_usuario = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('manual_de_usuario', i, fn), verbose_name=u'Manual de usuario', blank=True, null=True)
    manual_de_mantencion = models.FileField(upload_to=lambda i, fn: generate_uploaded_adquisicion_file_name('manual_de_mantencion', i, fn), verbose_name=u'Manual de mantención', blank=True, null=True)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición por compra'
        verbose_name_plural = u'Adquisiciones por compra'
