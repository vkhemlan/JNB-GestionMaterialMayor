# coding: utf-8
from django.conf import settings

from django.db import models
from django.db.models import Q
import os
from sorl.thumbnail import ImageField
from datetime import date

def generate_uploaded_material_mayor_file_name(field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)
    
    filename = 'documentos/material_mayor/%d/%s.%s' % (instance.id, field_name, extension)
    
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, filename))
    except OSError:
        pass
    
    return filename
    
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
    vin = models.CharField(max_length=255, verbose_name=u'VIN')
    numero_serie = models.CharField(max_length=255, verbose_name=u'Número de serie')
    peso_bruto_vehicular = models.PositiveIntegerField(verbose_name=u'Peso bruto vehicular')
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
    certificado_de_anotaciones_vigentes = models.ForeignKey('CambioCertificadoAnotacionesVigentes', blank=True, null=True)
    asignacion_solicitud_primera_inscripcion = models.ForeignKey('AsignacionSolicitudPrimeraInscripcion', blank=True, null=True)
    denominacion = models.CharField(max_length=255, blank=True, null=True)
    # Fotografías
    fotografia_frontal = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_frontal', i, fn), verbose_name=u'Vista Frontal', blank=True, null=True)
    fotografia_lateral = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_lateral', i, fn), verbose_name=u'Vista Lateral', blank=True, null=True)
    fotografia_trasera = ImageField(upload_to=lambda i, fn: uploaded_image_rename('fotografia_trasera', i, fn), verbose_name=u'Vista Trasera', blank=True, null=True)
    # Información de procesos asociados
    adquisicion = models.OneToOneField('AdquisicionMaterialMayor', blank=True, null=True)
    asignacion_de_patente = models.OneToOneField('AsignacionPatenteMaterialMayor', blank=True, null=True)
    dada_de_baja = models.OneToOneField('DadaDeBajaMaterialMayor', blank=True, null=True)
    # Metadata
    validado_por_operaciones = models.BooleanField(default=True)
    # Asociacion
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)
    compania = models.ForeignKey('Compania', blank=True, null=True)
    
    def __unicode__(self):
        return self.breadcrumbs_string()

    @classmethod
    def vehiculos_en_alta(cls):
        return cls.objects.filter(validado_por_operaciones=True, dada_de_baja__isnull=True)
        
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

    def notify_operaciones_of_asignacion_a_compania(self):
        from . import Rol, UserProfile
        operaciones_bomberiles_user_profiles = UserProfile.objects.filter(rol=Rol.OPERACIONES())
        for user_profile in operaciones_bomberiles_user_profiles:
            user_profile.send_asignacion_compania_email(self)

    def obtener_estado(self):
        if not self.validado_por_operaciones:
            return 'Sin validar'
        elif not self.dada_de_baja:
            return 'En servicio'
        else:
            return 'Dado de baja'

    def corresponde_mantenimiento_programado(self, frecuencia_operacion, fecha):
        fecha_crecion_vehiculo = self.adquisicion.fecha.date()

        if fecha == fecha_crecion_vehiculo:
            return False

        if fecha.day != fecha_crecion_vehiculo.day:
            return False

        month_difference = (fecha.year * 12 + fecha.month) - (fecha_crecion_vehiculo.year * 12 + fecha_crecion_vehiculo.month)

        return month_difference % frecuencia_operacion.numero_meses == 0

    def gatillar_operaciones_mantencion_manualmente(self, numero_meses):
        from . import FrecuenciaOperacion
        fecha_crecion_vehiculo = self.adquisicion.fecha.date()

        numero_total_meses = fecha_crecion_vehiculo.year * 12 + (fecha_crecion_vehiculo.month - 1) + numero_meses
        nuevo_numero_annos = numero_total_meses / 12
        nuevo_numero_meses = numero_total_meses % 12 + 1

        fecha_gatillo = date(nuevo_numero_annos, nuevo_numero_meses, fecha_crecion_vehiculo.day)

        self.revisar_nuevas_mantenciones_programadas(FrecuenciaOperacion.objects.all(), fecha_gatillo)

    def revisar_nuevas_mantenciones_programadas(self, frecuencias_operacion, fecha=date.today()):
        from . import OperacionMantencionPauta, MantencionProgramada, OperacionMantencionProgramada

        if not self.validado_por_operaciones:
            return

        ids_pautas_mantencion = [self.pauta_mantencion_carrosado.id, self.modelo_chasis.pauta_mantencion.id]
        ids_frecuencias_operacion_compatibles = [f.id for f in frecuencias_operacion if self.corresponde_mantenimiento_programado(f, fecha)]
        ids_operaciones_mantencion_pendientes = [op.id_operacion_mantencion_pauta for op in OperacionMantencionProgramada.objects.filter(ejecucion__isnull=True, mantencion__material_mayor=self)]

        operaciones_mantencion_compatibles = OperacionMantencionPauta.objects.filter(pauta__id__in=ids_pautas_mantencion, frecuencia__id__in=ids_frecuencias_operacion_compatibles).filter(~Q(id__in=ids_operaciones_mantencion_pendientes))

        if operaciones_mantencion_compatibles:
            mantencion_programada = MantencionProgramada(fecha=fecha, material_mayor=self)
            mantencion_programada.save()
            for operacion in operaciones_mantencion_compatibles:
                operacion_mantencion_programada = OperacionMantencionProgramada()
                operacion_mantencion_programada.id_operacion_mantencion_pauta = operacion.id
                operacion_mantencion_programada.descripcion = operacion.descripcion
                operacion_mantencion_programada.mantencion = mantencion_programada
                operacion_mantencion_programada.save()

    class Meta:
        app_label = 'interface'
        verbose_name = u'Material mayor'
        verbose_name_plural = u'Material mayor'
