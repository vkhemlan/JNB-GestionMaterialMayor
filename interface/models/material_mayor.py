# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField
from datetime import date

class MaterialMayor(models.Model):
    # Datos del vehículo
    tipo_vehiculo = models.ForeignKey('TipoVehiculoMaterialMayor', verbose_name=u'Tipo de vehículo')
    modelo_chasis = models.ForeignKey('ModeloChasisMaterialMayor', verbose_name=u'Modelo de chasis')
    numero_chasis = models.CharField(max_length=255, verbose_name=u'Numero de chasis')
    numero_motor = models.CharField(max_length=255, verbose_name=u'Número de motor')
    YEAR_CHOICES = [(year, year) for year in xrange(date.today().year, 1949, -1)]
    ano_vehiculo = models.IntegerField(choices=YEAR_CHOICES, verbose_name=u'Año del vehículo')
    color = models.ForeignKey('ColorMaterialMayor', verbose_name=u'Color')
    placa_patente = models.CharField(max_length=255, verbose_name=u'Placa patente')
    # Información adicional
    modelo_carrosado = models.ForeignKey('ModeloCarrosadoMaterialMayor', verbose_name=u'Modelo de carrosado')
    condicion = models.ForeignKey('CondicionMaterialMayor', verbose_name=u'Condición')
    modelo_caja_cambio = models.ForeignKey('ModeloCajaCambioMaterialMayor', verbose_name=u'Modelo de caja de cambio')
    tipo_caja_cambio = models.ForeignKey('TipoCajaCambioMaterialMayor', verbose_name=u'Tipo de caja de cambio')
    tipo_combustible = models.ForeignKey('TipoCombustibleMaterialMayor', verbose_name=u'Tipo de combustible')
    modelo_bomba = models.ForeignKey('ModeloBombaMaterialMayor', verbose_name=u'Modelo de bomba')
    pais_origen = models.ForeignKey('Pais', verbose_name=u'País de origen')
    # Fotografías
    fotografia_frontal = ImageField(upload_to='material_mayor', verbose_name=u'Vista Frontal')
    fotografia_lateral = ImageField(upload_to='material_mayor', verbose_name=u'Vista Lateral')
    fotografia_trasera = ImageField(upload_to='material_mayor', verbose_name=u'Vista Trasera')
    # Metadata
    adquisicion = models.OneToOneField('AdquisicionMaterialMayor')
    # Asociacion
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)
    compania = models.ForeignKey('Compania', blank=True, null=True)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Material Mayor'
        verbose_name_plural = u'Material Mayor'
