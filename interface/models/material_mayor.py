# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField
from datetime import date
from django.conf import settings

def generate_uploaded_material_mayor_file_name(field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'documentos/material_mayor/%d/%s.%s' % (instance.id, field_name, extension)
    
def uploaded_image_rename(field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'fotografias/material_mayor/%d/%s.%s' % (instance.id, field_name, extension)

class MaterialMayor(models.Model):
    # Datos del vehículo
    tipo_vehiculo = models.ForeignKey('TipoVehiculoMaterialMayor', verbose_name=u'Tipo de vehículo', blank=True, null=True)
    uso = models.ForeignKey('UsoMaterialMayor', blank=True, null=True)
    otro_uso = models.CharField(max_length=255, blank=True, null=True, verbose_name='Uso vehículo especial')
    modelo_chasis = models.ForeignKey('ModeloChasisMaterialMayor', verbose_name=u'Modelo de chasis')
    numero_chasis = models.CharField(max_length=255, verbose_name=u'Número de chasis')
    numero_motor = models.CharField(max_length=255, verbose_name=u'Número de motor')
    YEAR_CHOICES = [(year, year) for year in xrange(date.today().year, 1949, -1)]
    ano_vehiculo = models.IntegerField(choices=YEAR_CHOICES, verbose_name=u'Año del vehículo', blank=True, null=True)
    color = models.ForeignKey('ColorMaterialMayor', verbose_name=u'Color', blank=True, null=True)
    # Información adicional
    marca_carrosado = models.ForeignKey('MarcaCarrosadoMaterialMayor', verbose_name=u'Marca de carrosado')
    pauta_mantencion_carrosado = models.ForeignKey('PautaMantencionCarrosado', verbose_name=u'Pauta de mantención del carrosado', blank=True, null=True)
    condicion = models.ForeignKey('CondicionMaterialMayor', verbose_name=u'Condición', blank=True, null=True)
    tipo_caja_cambio = models.ForeignKey('TipoCajaCambioMaterialMayor', verbose_name=u'Tipo de caja de cambio', blank=True, null=True)
    modelo_caja_cambio = models.ForeignKey('ModeloCajaCambioMaterialMayor', verbose_name=u'Modelo de caja de cambio', blank=True, null=True)
    tipo_combustible = models.ForeignKey('TipoCombustibleMaterialMayor', verbose_name=u'Tipo de combustible', blank=True, null=True)
    modelo_bomba = models.ForeignKey('ModeloBombaMaterialMayor', verbose_name=u'Modelo de bomba', blank=True, null=True)
    pais_origen = models.ForeignKey('Pais', verbose_name=u'País de origen', blank=True, null=True)
    planos = models.FileField(upload_to=lambda i, fn: generate_uploaded_material_mayor_file_name('planos', i, fn), verbose_name=u'Planos del vehículo', blank=True, null=True)
    # Fotografías
    fotografia_frontal = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_frontal', i, fn), verbose_name=u'Vista Frontal', blank=True, null=True)
    fotografia_lateral = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_lateral', i, fn), verbose_name=u'Vista Lateral', blank=True, null=True)
    fotografia_trasera = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_trasera', i, fn), verbose_name=u'Vista Trasera', blank=True, null=True)
    # Metadata
    adquisicion = models.OneToOneField('AdquisicionMaterialMayor')
    asignacion_de_patente = models.OneToOneField('AsignacionPatenteMaterialMayor', blank=True, null=True)
    validado_por_operaciones = models.BooleanField(default=True)
    # Asociacion
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)
    compania = models.ForeignKey('Compania', blank=True, null=True)
    
    def __unicode__(self):
        return self.breadcrumbs_string()
        
    def extract_data(self, keys):
        return_data = []
        for key in keys:
            return_data.append(unicode(eval('self.%s' % key)))
        return {
            'data': return_data,
            'id': self.id
        }
        
    def get_location(self):
        if self.compania:
            return '%s - %s (%s)' % (unicode(self.compania), unicode(self.cuerpo), unicode(self.cuerpo.comuna.provincia.region))
        elif self.cuerpo:
            return '%s (%s) - Nivel central' % (unicode(self.cuerpo), unicode(self.cuerpo.comuna.provincia.region))
        else:
            return 'Nivel central JNBC'
            
    def breadcrumbs_string(self):
        return u'%s %s - N° chasis %s' % (unicode(self.modelo_chasis.marca), unicode(self.modelo_chasis), self.numero_chasis)
            
    def notify_operaciones_of_dada_de_alta(self):
        from . import Rol, UserProfile
        operaciones_bomberiles_user_profiles = UserProfile.objects.filter(rol=Rol.OPERACIONES())
        for user_profile in operaciones_bomberiles_user_profiles:
            user_profile.send_new_dada_de_alta_email(self)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Material mayor'
        verbose_name_plural = u'Material mayor'
