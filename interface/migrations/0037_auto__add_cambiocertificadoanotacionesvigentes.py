# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CambioCertificadoAnotacionesVigentes'
        db.create_table('interface_cambiocertificadoanotacionesvigentes', (
            ('eventohojavidamaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.EventoHojaVidaMaterialMayor'], unique=True, primary_key=True)),
            ('certificado_anotaciones_vigentes', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('interface', ['CambioCertificadoAnotacionesVigentes'])


    def backwards(self, orm):
        
        # Deleting model 'CambioCertificadoAnotacionesVigentes'
        db.delete_table('interface_cambiocertificadoanotacionesvigentes')


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
            'fecha_limitacion_dominio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
        'interface.asignacioncompaniamaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'AsignacionCompaniaMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']"}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'})
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
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'patente': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'certificado_de_anotaciones_vigentes': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ColorMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']", 'null': 'True', 'blank': 'True'}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.CondicionMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']", 'null': 'True', 'blank': 'True'}),
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
        'interface.operacionmantencion': {
            'Meta': {'ordering': "['id']", 'object_name': 'OperacionMantencion'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'frecuencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.FrecuenciaOperacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pauta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.PautaMantencion']"})
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
