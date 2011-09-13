# coding: utf-8

from django.db import models
from datetime import date

class MaterialMayor(models.Model):
    # Datos del vehículo
    tipo_vehiculo = models.ForeignKey('TipoVehiculoMaterialMayor', verbose_name=u'Tipo de vehículo')
    modelo_chasis = models.ForeignKey('ModeloChasisMaterialMayor', verbose_name=u'Modelo de chasis')
    numero_chasis = models.CharField(max_length=255, verbose_name=u'Numero de chasis')
    numero_motor = models.CharField(max_length=255, verbose_name=u'Número de motor')
    placa_patente = models.CharField(max_length=255, verbose_name=u'Placa patente')
    YEAR_CHOICES = [(year, year) for year in xrange(date.today().year, 1949, -1)]
    ano_vehiculo = models.IntegerField(choices=YEAR_CHOICES, verbose_name=u'Año del vehículo')
    color = models.ForeignKey('ColorMaterialMayor', verbose_name=u'Color')
    # Información adicional
    modelo_carrosado = models.ForeignKey('ModeloCarrosadoMaterialMayor', verbose_name=u'Modelo de carrosado')
    condicion = models.ForeignKey('CondicionMaterialMayor', verbose_name=u'Condición')
    modelo_caja_cambio = models.ForeignKey('ModeloCajaCambioMaterialMayor', verbose_name=u'Modelo de caja de cambio')
    tipo_caja_cambio = models.ForeignKey('TipoCajaCambioMaterialMayor', verbose_name=u'Tipo de caja de cambio')
    tipo_combustible = models.ForeignKey('TipoCombustibleMaterialMayor', verbose_name=u'Tipo de combustible')
    modelo_bomba = models.ForeignKey('ModeloBombaMaterialMayor', verbose_name=u'Modelo de bomba')
    pais_origen = models.ForeignKey('Pais', verbose_name=u'País de origen')
    

    class Meta:
        app_label = 'interface'
        verbose_name = u'Material Mayor'
        verbose_name_plural = u'Material Mayor'
