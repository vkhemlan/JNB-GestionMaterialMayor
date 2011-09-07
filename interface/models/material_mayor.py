# coding: utf-8

from django.db import models
from datetime import date

class MaterialMayor(models.Model):
    tipo_vehiculo = models.ForeignKey('TipoVehiculoMaterialMayor', verbose_name=u'Tipo de vehículo')
    marca_chasis = models.ForeignKey('MarcaChasisMaterialMayor', verbose_name=u'Marca de chasis')
    modelo_chasis = models.CharField(max_length=255, verbose_name=u'Modelo de chasis')
    numero_chasis = models.CharField(max_length=255, verbose_name=u'Numero de chasis')
    numero_motor = models.CharField(max_length=255, verbose_name=u'Número de motor')
    placa_patente = models.CharField(max_length=255, verbose_name=u'Placa patente')
    YEAR_CHOICES = [(year, year) for year in xrange(date.today().year, 1949, -1)]
    ano_vehiculo = models.IntegerField(choices=YEAR_CHOICES, verbose_name=u'Año del vehículo')
    color = models.ForeignKey('ColorMaterialMayor', verbose_name=u'Color')
    
    class Meta:
        app_label = 'interface'
        verbose_name = u'Material Mayor'
        verbose_name_plural = u'Material Mayor'