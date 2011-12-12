# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FrecuenciaOperacion'
        db.create_table('interface_frecuenciaoperacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero_meses', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('interface', ['FrecuenciaOperacion'])

        # Adding model 'PautaMantencion'
        db.create_table('interface_pautamantencion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['PautaMantencion'])

        # Adding model 'PautaMantencionChasis'
        db.create_table('interface_pautamantencionchasis', (
            ('pautamantencion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.PautaMantencion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('interface', ['PautaMantencionChasis'])

        # Adding model 'PautaMantencionCarrosado'
        db.create_table('interface_pautamantencioncarrosado', (
            ('pautamantencion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.PautaMantencion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('interface', ['PautaMantencionCarrosado'])

        # Adding model 'FamiliaUsoMaterialMayor'
        db.create_table('interface_familiausomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['FamiliaUsoMaterialMayor'])

        # Adding model 'UsoMaterialMayor'
        db.create_table('interface_usomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('familia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.FamiliaUsoMaterialMayor'])),
            ('is_others_option', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('interface', ['UsoMaterialMayor'])

        # Adding model 'TipoVehiculoMaterialMayor'
        db.create_table('interface_tipovehiculomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['TipoVehiculoMaterialMayor'])

        # Adding model 'MarcaChasisMaterialMayor'
        db.create_table('interface_marcachasismaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaChasisMaterialMayor'])

        # Adding model 'ColorMaterialMayor'
        db.create_table('interface_colormaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ColorMaterialMayor'])

        # Adding model 'MaterialMayor'
        db.create_table('interface_materialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoVehiculoMaterialMayor'], null=True, blank=True)),
            ('uso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.UsoMaterialMayor'], null=True, blank=True)),
            ('otro_uso', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('modelo_chasis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloChasisMaterialMayor'])),
            ('numero_chasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero_motor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ano_vehiculo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ColorMaterialMayor'], null=True, blank=True)),
            ('marca_carrosado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaCarrosadoMaterialMayor'])),
            ('pauta_mantencion_carrosado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.PautaMantencionCarrosado'], null=True, blank=True)),
            ('condicion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.CondicionMaterialMayor'], null=True, blank=True)),
            ('tipo_caja_cambio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCajaCambioMaterialMayor'], null=True, blank=True)),
            ('modelo_caja_cambio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloCajaCambioMaterialMayor'], null=True, blank=True)),
            ('tipo_combustible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCombustibleMaterialMayor'], null=True, blank=True)),
            ('modelo_bomba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloBombaMaterialMayor'], null=True, blank=True)),
            ('pais_origen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Pais'], null=True, blank=True)),
            ('planos', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('certificado_de_anotaciones_vigentes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.CambioCertificadoAnotacionesVigentes'], null=True, blank=True)),
            ('asignacion_solicitud_primera_inscripcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.AsignacionSolicitudPrimeraInscripcion'], null=True, blank=True)),
            ('fotografia_frontal', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('fotografia_lateral', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('fotografia_trasera', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('adquisicion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True)),
            ('asignacion_de_patente', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AsignacionPatenteMaterialMayor'], unique=True, null=True, blank=True)),
            ('dada_de_baja', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.DadaDeBajaMaterialMayor'], unique=True, null=True, blank=True)),
            ('validado_por_operaciones', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'], null=True, blank=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Compania'], null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['MaterialMayor'])

        # Adding model 'ModeloChasisMaterialMayor'
        db.create_table('interface_modelochasismaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaChasisMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pauta_mantencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.PautaMantencionChasis'])),
        ))
        db.send_create_signal('interface', ['ModeloChasisMaterialMayor'])

        # Adding model 'MarcaCarrosadoMaterialMayor'
        db.create_table('interface_marcacarrosadomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaCarrosadoMaterialMayor'])

        # Adding model 'CondicionMaterialMayor'
        db.create_table('interface_condicionmaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['CondicionMaterialMayor'])

        # Adding model 'MarcaCajaCambioMaterialMayor'
        db.create_table('interface_marcacajacambiomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaCajaCambioMaterialMayor'])

        # Adding model 'ModeloCajaCambioMaterialMayor'
        db.create_table('interface_modelocajacambiomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaCajaCambioMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModeloCajaCambioMaterialMayor'])

        # Adding model 'TipoCajaCambioMaterialMayor'
        db.create_table('interface_tipocajacambiomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['TipoCajaCambioMaterialMayor'])

        # Adding model 'TipoCombustibleMaterialMayor'
        db.create_table('interface_tipocombustiblematerialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['TipoCombustibleMaterialMayor'])

        # Adding model 'MarcaBombaMaterialMayor'
        db.create_table('interface_marcabombamaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaBombaMaterialMayor'])

        # Adding model 'ModeloBombaMaterialMayor'
        db.create_table('interface_modelobombamaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaBombaMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModeloBombaMaterialMayor'])

        # Adding model 'Pais'
        db.create_table('interface_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['Pais'])

        # Adding model 'AdquisicionMaterialMayor'
        db.create_table('interface_adquisicionmaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModoAdquisicionMaterialMayor'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cuerpo_destinatario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'])),
        ))
        db.send_create_signal('interface', ['AdquisicionMaterialMayor'])

        # Adding model 'AdquisicionCompraMaterialMayor'
        db.create_table('interface_adquisicioncompramaterialmayor', (
            ('adquisicionmaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True, primary_key=True)),
            ('orden_de_compra', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('numero_orden_de_compra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fecha_orden_de_compra', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('numero_declaracion_de_ingreso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fecha_declaracion_de_ingreso', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('factura_comercial', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('bill_of_lading', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('packing_list', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('acta_de_recepcion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('respuesta_solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('valor_final_de_compra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('proveedor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('agente_de_aduana', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('manual_de_usuario', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('manual_de_mantencion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['AdquisicionCompraMaterialMayor'])

        # Adding model 'AdquisicionDonacionMaterialMayor'
        db.create_table('interface_adquisiciondonacionmaterialmayor', (
            ('adquisicionmaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True, primary_key=True)),
            ('donante', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('forma_adquisicion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_vencimiento_limitacion_dominio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dueno_comodato', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('factura', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('bill_of_lading', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('packing_list', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['AdquisicionDonacionMaterialMayor'])

        # Adding model 'ModoAdquisicionMaterialMayor'
        db.create_table('interface_modoadquisicionmaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModoAdquisicionMaterialMayor'])

        # Adding model 'Region'
        db.create_table('interface_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['Region'])

        # Adding model 'Provincia'
        db.create_table('interface_provincia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Region'])),
        ))
        db.send_create_signal('interface', ['Provincia'])

        # Adding model 'Comuna'
        db.create_table('interface_comuna', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Provincia'])),
        ))
        db.send_create_signal('interface', ['Comuna'])

        # Adding model 'Cuerpo'
        db.create_table('interface_cuerpo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comuna', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Comuna'])),
        ))
        db.send_create_signal('interface', ['Cuerpo'])

        # Adding model 'Compania'
        db.create_table('interface_compania', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'])),
        ))
        db.send_create_signal('interface', ['Compania'])

        # Adding model 'TipoEventoHojaVidaMaterialMayor'
        db.create_table('interface_tipoeventohojavidamaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['TipoEventoHojaVidaMaterialMayor'])

        # Adding model 'EventoHojaVidaMaterialMayor'
        db.create_table('interface_eventohojavidamaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material_mayor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MaterialMayor'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rol_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Rol'], null=True, blank=True)),
            ('cuerpo_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'], null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoEventoHojaVidaMaterialMayor'])),
        ))
        db.send_create_signal('interface', ['EventoHojaVidaMaterialMayor'])

        # Adding M2M table for field cargos_usuario on 'EventoHojaVidaMaterialMayor'
        db.create_table('interface_eventohojavidamaterialmayor_cargos_usuario', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventohojavidamaterialmayor', models.ForeignKey(orm['interface.eventohojavidamaterialmayor'], null=False)),
            ('cargo', models.ForeignKey(orm['interface.cargo'], null=False))
        ))
        db.create_unique('interface_eventohojavidamaterialmayor_cargos_usuario', ['eventohojavidamaterialmayor_id', 'cargo_id'])

        # Adding model 'AsignacionCuerpoMaterialMayor'
        db.create_table('interface_asignacioncuerpomaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'])),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Compania'], null=True, blank=True)),
            ('fecha_de_asignacion', self.gf('django.db.models.fields.DateField')()),
            ('acta_de_entrega_de_asignacion', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('listado_de_material_menor', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('transferencia_por_escritura_publica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_de_escritura', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('escritura_publica', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('notaria', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numero_de_repertorio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['AsignacionCuerpoMaterialMayor'])

        # Adding model 'AsignacionCompaniaMaterialMayor'
        db.create_table('interface_asignacioncompaniamaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Compania'])),
            ('numero_orden_del_dia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_orden_del_dia', self.gf('django.db.models.fields.DateField')()),
            ('orden_del_dia', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['AsignacionCompaniaMaterialMayor'])

        # Adding model 'Rol'
        db.create_table('interface_rol', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['Rol'])

        # Adding model 'Cargo'
        db.create_table('interface_cargo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['Cargo'])

        # Adding model 'UserProfile'
        db.create_table('interface_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('webservice_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Rol'], null=True, blank=True)),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'], null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['UserProfile'])

        # Adding M2M table for field cargos on 'UserProfile'
        db.create_table('interface_userprofile_cargos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['interface.userprofile'], null=False)),
            ('cargo', models.ForeignKey(orm['interface.cargo'], null=False))
        ))
        db.create_unique('interface_userprofile_cargos', ['userprofile_id', 'cargo_id'])

        # Adding model 'AsignacionPatenteMaterialMayor'
        db.create_table('interface_asignacionpatentematerialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('patente', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('digito_verificador', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['AsignacionPatenteMaterialMayor'])

        # Adding model 'CambioPautaMantencionCarrosadoMaterialMayor'
        db.create_table('interface_cambiopautamantencioncarrosadomaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('nueva_pauta_mantencion_carrosado', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['CambioPautaMantencionCarrosadoMaterialMayor'])

        # Adding model 'CambioNumeroChasisMaterialMayor'
        db.create_table('interface_cambionumerochasismaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('nuevo_numero_chasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['CambioNumeroChasisMaterialMayor'])

        # Adding model 'CambioNumeroMotorMaterialMayor'
        db.create_table('interface_cambionumeromotormaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('nuevo_numero_motor', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['CambioNumeroMotorMaterialMayor'])

        # Adding model 'CambioCertificadoAnotacionesVigentes'
        db.create_table('interface_cambiocertificadoanotacionesvigentes', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('certificado_anotaciones_vigentes', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('interface', ['CambioCertificadoAnotacionesVigentes'])

        # Adding model 'AsignacionSolicitudPrimeraInscripcion'
        db.create_table('interface_asignacionsolicitudprimerainscripcion', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('solicitud_primera_inscripcion', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('interface', ['AsignacionSolicitudPrimeraInscripcion'])

        # Adding model 'OperacionMantencionPauta'
        db.create_table('interface_operacionmantencionpauta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pauta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.PautaMantencion'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('frecuencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.FrecuenciaOperacion'])),
        ))
        db.send_create_signal('interface', ['OperacionMantencionPauta'])

        # Adding model 'OperacionMantencionProgramada'
        db.create_table('interface_operacionmantencionprogramada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mantencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MantencionProgramada'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('ejecucion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EjecucionOperacionMantencionProgramada'], unique=True, null=True, blank=True)),
            ('id_operacion_mantencion_pauta', self.gf('django.db.models.fields.IntegerField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['OperacionMantencionProgramada'])

        # Adding model 'MantencionProgramada'
        db.create_table('interface_mantencionprogramada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material_mayor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MaterialMayor'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('interface', ['MantencionProgramada'])

        # Adding model 'EjecucionOperacionMantencionProgramada'
        db.create_table('interface_ejecucionoperacionmantencionprogramada', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('interface', ['EjecucionOperacionMantencionProgramada'])

        # Adding model 'ArchivoMantencionProgramada'
        db.create_table('interface_archivomantencionprogramada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('mantencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MantencionProgramada'])),
        ))
        db.send_create_signal('interface', ['ArchivoMantencionProgramada'])

        # Adding model 'MotivoDadaDeBaja'
        db.create_table('interface_motivodadadebaja', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MotivoDadaDeBaja'])

        # Adding model 'DadaDeBajaMaterialMayor'
        db.create_table('interface_dadadebajamaterialmayor', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MotivoDadaDeBaja'])),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['DadaDeBajaMaterialMayor'])


    def backwards(self, orm):
        
        # Deleting model 'FrecuenciaOperacion'
        db.delete_table('interface_frecuenciaoperacion')

        # Deleting model 'PautaMantencion'
        db.delete_table('interface_pautamantencion')

        # Deleting model 'PautaMantencionChasis'
        db.delete_table('interface_pautamantencionchasis')

        # Deleting model 'PautaMantencionCarrosado'
        db.delete_table('interface_pautamantencioncarrosado')

        # Deleting model 'FamiliaUsoMaterialMayor'
        db.delete_table('interface_familiausomaterialmayor')

        # Deleting model 'UsoMaterialMayor'
        db.delete_table('interface_usomaterialmayor')

        # Deleting model 'TipoVehiculoMaterialMayor'
        db.delete_table('interface_tipovehiculomaterialmayor')

        # Deleting model 'MarcaChasisMaterialMayor'
        db.delete_table('interface_marcachasismaterialmayor')

        # Deleting model 'ColorMaterialMayor'
        db.delete_table('interface_colormaterialmayor')

        # Deleting model 'MaterialMayor'
        db.delete_table('interface_materialmayor')

        # Deleting model 'ModeloChasisMaterialMayor'
        db.delete_table('interface_modelochasismaterialmayor')

        # Deleting model 'MarcaCarrosadoMaterialMayor'
        db.delete_table('interface_marcacarrosadomaterialmayor')

        # Deleting model 'CondicionMaterialMayor'
        db.delete_table('interface_condicionmaterialmayor')

        # Deleting model 'MarcaCajaCambioMaterialMayor'
        db.delete_table('interface_marcacajacambiomaterialmayor')

        # Deleting model 'ModeloCajaCambioMaterialMayor'
        db.delete_table('interface_modelocajacambiomaterialmayor')

        # Deleting model 'TipoCajaCambioMaterialMayor'
        db.delete_table('interface_tipocajacambiomaterialmayor')

        # Deleting model 'TipoCombustibleMaterialMayor'
        db.delete_table('interface_tipocombustiblematerialmayor')

        # Deleting model 'MarcaBombaMaterialMayor'
        db.delete_table('interface_marcabombamaterialmayor')

        # Deleting model 'ModeloBombaMaterialMayor'
        db.delete_table('interface_modelobombamaterialmayor')

        # Deleting model 'Pais'
        db.delete_table('interface_pais')

        # Deleting model 'AdquisicionMaterialMayor'
        db.delete_table('interface_adquisicionmaterialmayor')

        # Deleting model 'AdquisicionCompraMaterialMayor'
        db.delete_table('interface_adquisicioncompramaterialmayor')

        # Deleting model 'AdquisicionDonacionMaterialMayor'
        db.delete_table('interface_adquisiciondonacionmaterialmayor')

        # Deleting model 'ModoAdquisicionMaterialMayor'
        db.delete_table('interface_modoadquisicionmaterialmayor')

        # Deleting model 'Region'
        db.delete_table('interface_region')

        # Deleting model 'Provincia'
        db.delete_table('interface_provincia')

        # Deleting model 'Comuna'
        db.delete_table('interface_comuna')

        # Deleting model 'Cuerpo'
        db.delete_table('interface_cuerpo')

        # Deleting model 'Compania'
        db.delete_table('interface_compania')

        # Deleting model 'TipoEventoHojaVidaMaterialMayor'
        db.delete_table('interface_tipoeventohojavidamaterialmayor')

        # Deleting model 'EventoHojaVidaMaterialMayor'
        db.delete_table('interface_eventohojavidamaterialmayor')

        # Removing M2M table for field cargos_usuario on 'EventoHojaVidaMaterialMayor'
        db.delete_table('interface_eventohojavidamaterialmayor_cargos_usuario')

        # Deleting model 'AsignacionCuerpoMaterialMayor'
        db.delete_table('interface_asignacioncuerpomaterialmayor')

        # Deleting model 'AsignacionCompaniaMaterialMayor'
        db.delete_table('interface_asignacioncompaniamaterialmayor')

        # Deleting model 'Rol'
        db.delete_table('interface_rol')

        # Deleting model 'Cargo'
        db.delete_table('interface_cargo')

        # Deleting model 'UserProfile'
        db.delete_table('interface_userprofile')

        # Removing M2M table for field cargos on 'UserProfile'
        db.delete_table('interface_userprofile_cargos')

        # Deleting model 'AsignacionPatenteMaterialMayor'
        db.delete_table('interface_asignacionpatentematerialmayor')

        # Deleting model 'CambioPautaMantencionCarrosadoMaterialMayor'
        db.delete_table('interface_cambiopautamantencioncarrosadomaterialmayor')

        # Deleting model 'CambioNumeroChasisMaterialMayor'
        db.delete_table('interface_cambionumerochasismaterialmayor')

        # Deleting model 'CambioNumeroMotorMaterialMayor'
        db.delete_table('interface_cambionumeromotormaterialmayor')

        # Deleting model 'CambioCertificadoAnotacionesVigentes'
        db.delete_table('interface_cambiocertificadoanotacionesvigentes')

        # Deleting model 'AsignacionSolicitudPrimeraInscripcion'
        db.delete_table('interface_asignacionsolicitudprimerainscripcion')

        # Deleting model 'OperacionMantencionPauta'
        db.delete_table('interface_operacionmantencionpauta')

        # Deleting model 'OperacionMantencionProgramada'
        db.delete_table('interface_operacionmantencionprogramada')

        # Deleting model 'MantencionProgramada'
        db.delete_table('interface_mantencionprogramada')

        # Deleting model 'EjecucionOperacionMantencionProgramada'
        db.delete_table('interface_ejecucionoperacionmantencionprogramada')

        # Deleting model 'ArchivoMantencionProgramada'
        db.delete_table('interface_archivomantencionprogramada')

        # Deleting model 'MotivoDadaDeBaja'
        db.delete_table('interface_motivodadadebaja')

        # Deleting model 'DadaDeBajaMaterialMayor'
        db.delete_table('interface_dadadebajamaterialmayor')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'interface.adquisicioncompramaterialmayor': {
            'Meta': {'object_name': 'AdquisicionCompraMaterialMayor', '_ormbases': ['interface.AdquisicionMaterialMayor']},
            'acta_de_recepcion': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adquisicionmaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.AdquisicionMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'agente_de_aduana': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_of_lading': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'declaracion_de_ingreso': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'factura_comercial': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha_declaracion_de_ingreso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_orden_de_compra': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'manual_de_mantencion': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'manual_de_usuario': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero_declaracion_de_ingreso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numero_orden_de_compra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orden_de_compra': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'packing_list': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respuesta_solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'valor_final_de_compra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'interface.adquisiciondonacionmaterialmayor': {
            'Meta': {'object_name': 'AdquisicionDonacionMaterialMayor', '_ormbases': ['interface.AdquisicionMaterialMayor']},
            'adquisicionmaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.AdquisicionMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'bill_of_lading': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'declaracion_de_ingreso': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'donante': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dueno_comodato': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'factura': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha_vencimiento_limitacion_dominio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'forma_adquisicion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'packing_list': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'interface.adquisicionmaterialmayor': {
            'Meta': {'object_name': 'AdquisicionMaterialMayor'},
            'cuerpo_destinatario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModoAdquisicionMaterialMayor']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'interface.archivomantencionprogramada': {
            'Meta': {'object_name': 'ArchivoMantencionProgramada'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantencion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MantencionProgramada']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.asignacioncompaniamaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'AsignacionCompaniaMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']"}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'fecha_orden_del_dia': ('django.db.models.fields.DateField', [], {}),
            'numero_orden_del_dia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'orden_del_dia': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'interface.asignacioncuerpomaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'AsignacionCuerpoMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'acta_de_entrega_de_asignacion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']"}),
            'escritura_publica': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'fecha_de_asignacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_de_escritura': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'listado_de_material_menor': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'notaria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'numero_de_repertorio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'transferencia_por_escritura_publica': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'interface.asignacionpatentematerialmayor': {
            'Meta': {'ordering': "['patente']", 'object_name': 'AsignacionPatenteMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'digito_verificador': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'patente': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'interface.asignacionsolicitudprimerainscripcion': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'AsignacionSolicitudPrimeraInscripcion', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'solicitud_primera_inscripcion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'interface.cambiocertificadoanotacionesvigentes': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'CambioCertificadoAnotacionesVigentes', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'certificado_anotaciones_vigentes': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'interface.cambionumerochasismaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'CambioNumeroChasisMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'nuevo_numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.cambionumeromotormaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'CambioNumeroMotorMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'nuevo_numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.cambiopautamantencioncarrosadomaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'CambioPautaMantencionCarrosadoMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'nueva_pauta_mantencion_carrosado': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.cargo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cargo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.colormaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'ColorMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.compania': {
            'Meta': {'ordering': "['cuerpo', 'numero']", 'object_name': 'Compania'},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.comuna': {
            'Meta': {'ordering': "['provincia', 'nombre']", 'object_name': 'Comuna'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Provincia']"}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.condicionmaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'CondicionMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.cuerpo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cuerpo'},
            'comuna': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Comuna']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.dadadebajamaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'DadaDeBajaMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MotivoDadaDeBaja']"}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'interface.ejecucionoperacionmantencionprogramada': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'EjecucionOperacionMantencionProgramada', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'interface.eventohojavidamaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'EventoHojaVidaMaterialMayor'},
            'cargos_usuario': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['interface.Cargo']", 'null': 'True', 'blank': 'True'}),
            'cuerpo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_mayor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MaterialMayor']"}),
            'rol_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Rol']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoEventoHojaVidaMaterialMayor']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'interface.familiausomaterialmayor': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'FamiliaUsoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.frecuenciaoperacion': {
            'Meta': {'ordering': "['numero_meses']", 'object_name': 'FrecuenciaOperacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_meses': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.mantencionprogramada': {
            'Meta': {'object_name': 'MantencionProgramada'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_mayor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MaterialMayor']"})
        },
        'interface.marcabombamaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'MarcaBombaMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.marcacajacambiomaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'MarcaCajaCambioMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.marcacarrosadomaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'MarcaCarrosadoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.marcachasismaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'MarcaChasisMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.materialmayor': {
            'Meta': {'object_name': 'MaterialMayor'},
            'adquisicion': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.AdquisicionMaterialMayor']", 'unique': 'True'}),
            'ano_vehiculo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'asignacion_de_patente': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.AsignacionPatenteMaterialMayor']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'asignacion_solicitud_primera_inscripcion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.AsignacionSolicitudPrimeraInscripcion']", 'null': 'True', 'blank': 'True'}),
            'certificado_de_anotaciones_vigentes': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.CambioCertificadoAnotacionesVigentes']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ColorMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']", 'null': 'True', 'blank': 'True'}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.CondicionMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']", 'null': 'True', 'blank': 'True'}),
            'dada_de_baja': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.DadaDeBajaMaterialMayor']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'fotografia_frontal': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fotografia_lateral': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fotografia_trasera': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca_carrosado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaCarrosadoMaterialMayor']"}),
            'modelo_bomba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloBombaMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'modelo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCajaCambioMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'modelo_chasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloChasisMaterialMayor']"}),
            'numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'otro_uso': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pais_origen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Pais']", 'null': 'True', 'blank': 'True'}),
            'pauta_mantencion_carrosado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.PautaMantencionCarrosado']", 'null': 'True', 'blank': 'True'}),
            'planos': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCajaCambioMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'tipo_combustible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCombustibleMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoVehiculoMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'uso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.UsoMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'validado_por_operaciones': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'interface.modelobombamaterialmayor': {
            'Meta': {'ordering': "['marca', 'name']", 'object_name': 'ModeloBombaMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaBombaMaterialMayor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.modelocajacambiomaterialmayor': {
            'Meta': {'ordering': "['marca', 'name']", 'object_name': 'ModeloCajaCambioMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaCajaCambioMaterialMayor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.modelochasismaterialmayor': {
            'Meta': {'ordering': "['marca', 'name']", 'object_name': 'ModeloChasisMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaChasisMaterialMayor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pauta_mantencion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.PautaMantencionChasis']"})
        },
        'interface.modoadquisicionmaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'ModoAdquisicionMaterialMayor'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.motivodadadebaja': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'MotivoDadaDeBaja'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.operacionmantencionpauta': {
            'Meta': {'ordering': "['id']", 'object_name': 'OperacionMantencionPauta'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'frecuencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.FrecuenciaOperacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pauta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.PautaMantencion']"})
        },
        'interface.operacionmantencionprogramada': {
            'Meta': {'ordering': "['id']", 'object_name': 'OperacionMantencionProgramada'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'ejecucion': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EjecucionOperacionMantencionProgramada']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_operacion_mantencion_pauta': ('django.db.models.fields.IntegerField', [], {}),
            'mantencion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MantencionProgramada']"}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'interface.pais': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.pautamantencion': {
            'Meta': {'ordering': "['name']", 'object_name': 'PautaMantencion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.pautamantencioncarrosado': {
            'Meta': {'ordering': "['name']", 'object_name': 'PautaMantencionCarrosado', '_ormbases': ['interface.PautaMantencion']},
            'pautamantencion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.PautaMantencion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'interface.pautamantencionchasis': {
            'Meta': {'ordering': "['name']", 'object_name': 'PautaMantencionChasis', '_ormbases': ['interface.PautaMantencion']},
            'pautamantencion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.PautaMantencion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'interface.provincia': {
            'Meta': {'ordering': "['region', 'nombre']", 'object_name': 'Provincia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Region']"}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.region': {
            'Meta': {'ordering': "['numero']", 'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.rol': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Rol'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.tipocajacambiomaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'TipoCajaCambioMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.tipocombustiblematerialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'TipoCombustibleMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.tipoeventohojavidamaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'TipoEventoHojaVidaMaterialMayor'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.tipovehiculomaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'TipoVehiculoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'cargos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['interface.Cargo']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Rol']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'interface.usomaterialmayor': {
            'Meta': {'ordering': "['familia', 'nombre']", 'object_name': 'UsoMaterialMayor'},
            'familia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.FamiliaUsoMaterialMayor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_others_option': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['interface']
