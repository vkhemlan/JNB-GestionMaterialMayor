# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField
from datetime import date

class MaterialMayor(models.Model):
    # Datos del vehículo
    tipo_vehiculo = models.ForeignKey('TipoVehiculoMaterialMayor', verbose_name=u'Tipo de vehículo', blank=True, null=True)
    modelo_chasis = models.ForeignKey('ModeloChasisMaterialMayor', verbose_name=u'Modelo de chasis')
    numero_chasis = models.CharField(max_length=255, verbose_name=u'Numero de chasis')
    numero_motor = models.CharField(max_length=255, verbose_name=u'Número de motor')
    YEAR_CHOICES = [(year, year) for year in xrange(date.today().year, 1949, -1)]
    ano_vehiculo = models.IntegerField(choices=YEAR_CHOICES, verbose_name=u'Año del vehículo', blank=True, null=True)
    color = models.ForeignKey('ColorMaterialMayor', verbose_name=u'Color', blank=True, null=True)
    # Información adicional
    marca_carrosado = models.ForeignKey('MarcaCarrosadoMaterialMayor', verbose_name=u'Marca de carrosado')
    condicion = models.ForeignKey('CondicionMaterialMayor', verbose_name=u'Condición', blank=True, null=True)
    tipo_caja_cambio = models.ForeignKey('TipoCajaCambioMaterialMayor', verbose_name=u'Tipo de caja de cambio', blank=True, null=True)
    modelo_caja_cambio = models.ForeignKey('ModeloCajaCambioMaterialMayor', verbose_name=u'Modelo de caja de cambio', blank=True, null=True)
    tipo_combustible = models.ForeignKey('TipoCombustibleMaterialMayor', verbose_name=u'Tipo de combustible', blank=True, null=True)
    modelo_bomba = models.ForeignKey('ModeloBombaMaterialMayor', verbose_name=u'Modelo de bomba', blank=True, null=True)
    pais_origen = models.ForeignKey('Pais', verbose_name=u'País de origen', blank=True, null=True)
    planos = models.FileField(upload_to='planos', verbose_name=u'Planos del vehículo', blank=True, null=True)
    # Fotografías
    fotografia_frontal = ImageField(upload_to='material_mayor', verbose_name=u'Vista Frontal', blank=True, null=True)
    fotografia_lateral = ImageField(upload_to='material_mayor', verbose_name=u'Vista Lateral', blank=True, null=True)
    fotografia_trasera = ImageField(upload_to='material_mayor', verbose_name=u'Vista Trasera', blank=True, null=True)
    # Metadata
    adquisicion = models.OneToOneField('AdquisicionMaterialMayor')
    # Asociacion
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)
    compania = models.ForeignKey('Compania', blank=True, null=True)
    
    def __unicode__(self):
        return '%s %s' % (unicode(self.tipo_vehiculo), unicode(self.modelo_chasis),)
        
    def get_location(self):
        if self.compania:
            return '%s - %s (%s)' % (unicode(self.compania), unicode(self.cuerpo), unicode(self.cuerpo.comuna.provincia.region))
        elif self.cuerpo:
            return '%s (%s) - Nivel central' % (unicode(self.cuerpo), unicode(self.cuerpo.comuna.provincia.region))
        else:
            return 'Nivel central JNBC'

    class Meta:
        app_label = 'interface'
        verbose_name = u'Material mayor'
        verbose_name_plural = u'Material mayor'
