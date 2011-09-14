# coding: utf-8

from django.db import models
from . import MaterialMayor

class AdquisicionCompraMaterialMayor(MaterialMayor):
    orden_de_compra = models.FileField(upload_to='ordenes_de_compra', verbose_name=u'Orden de compra')
    numero_orden_de_compra = models.IntegerField(verbose_name=u'Número de orden de compra')
    fecha_orden_de_compra = models.DateField(verbose_name=u'Fecha de orden de compra')
    factura_comercial = models.FileField(upload_to='facturas_comerciales', verbose_name=u'Factura Comercial')
    bill_of_lading = models.FileField(upload_to='bills_of_lading', verbose_name=u'Bill of Lading')
    packing_list = models.FileField(upload_to='packing_lists', verbose_name=u'Packing List')
    declaracion_de_ingreso = models.FileField(upload_to='declaraciones_de_ingreso', verbose_name=u'Declaración de Ingreso')
    numero_declaracion_de_ingreso = models.IntegerField(verbose_name=u'Número de declaración de ingreso')
    fecha_declaracion_de_ingreso = models.DateField(verbose_name=u'Fecha de declaración de ingreso')
    solicitud_exencion_de_iva = models.FileField(upload_to='solicitudes_exencion_de_iva', verbose_name=u'Solicitud de exención de IVA')
    respuesta_solicitud_exencion_de_iva = models.FileField(upload_to='respuestas_solicitud_exencion_de_iva', verbose_name=u'Respuesta solicitud de exención de IVA')
    acta_de_recepcion = models.FileField(upload_to='actas_de_recepcion', verbose_name=u'Acta de recepción')
    valor_final_de_compra = models.IntegerField(verbose_name=u'Valor final de la compra')
    agente_de_aduana = models.CharField(max_length=255, verbose_name=u'Agente de aduana')
    manual_de_usuario = models.FileField(upload_to='manuales_de_usuario', verbose_name=u'Manual de usuario')
    manual_de_mantencion = models.FileField(upload_to='manuales_de_mantencion', verbose_name=u'Manual de mantención')

    def __unicode__(self):
        return unicode(self.materialmayor_ptr)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Adquisición por compra de Material Mayor'
        verbose_name_plural = u'Adquisiciones por compra de Material Mayor'