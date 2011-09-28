# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AdquisicionCompraMaterialMayor.proveedor'
        db.add_column('interface_adquisicioncompramaterialmayor', 'proveedor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Changing field 'AdquisicionCompraMaterialMayor.orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'orden_de_compra', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.valor_final_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'valor_final_de_compra', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.bill_of_lading'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'bill_of_lading', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.packing_list'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'packing_list', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.acta_de_recepcion'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'acta_de_recepcion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.numero_orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'numero_orden_de_compra', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.fecha_declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'fecha_declaracion_de_ingreso', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.numero_declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'numero_declaracion_de_ingreso', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.factura_comercial'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'factura_comercial', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.respuesta_solicitud_exencion_de_iva'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'respuesta_solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.solicitud_exencion_de_iva'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.manual_de_mantencion'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'manual_de_mantencion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.fecha_orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'fecha_orden_de_compra', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.agente_de_aduana'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'agente_de_aduana', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'AdquisicionCompraMaterialMayor.manual_de_usuario'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'manual_de_usuario', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'MaterialMayor.pais_origen'
        db.alter_column('interface_materialmayor', 'pais_origen_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Pais'], null=True))

        # Changing field 'MaterialMayor.tipo_combustible'
        db.alter_column('interface_materialmayor', 'tipo_combustible_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCombustibleMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.modelo_caja_cambio'
        db.alter_column('interface_materialmayor', 'modelo_caja_cambio_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloCajaCambioMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.planos'
        db.alter_column('interface_materialmayor', 'planos', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'MaterialMayor.color'
        db.alter_column('interface_materialmayor', 'color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ColorMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.fotografia_trasera'
        db.alter_column('interface_materialmayor', 'fotografia_trasera', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'MaterialMayor.fotografia_frontal'
        db.alter_column('interface_materialmayor', 'fotografia_frontal', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'MaterialMayor.modelo_bomba'
        db.alter_column('interface_materialmayor', 'modelo_bomba_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloBombaMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.fotografia_lateral'
        db.alter_column('interface_materialmayor', 'fotografia_lateral', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'MaterialMayor.condicion'
        db.alter_column('interface_materialmayor', 'condicion_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.CondicionMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.tipo_caja_cambio'
        db.alter_column('interface_materialmayor', 'tipo_caja_cambio_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCajaCambioMaterialMayor'], null=True))

        # Changing field 'MaterialMayor.ano_vehiculo'
        db.alter_column('interface_materialmayor', 'ano_vehiculo', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MaterialMayor.tipo_vehiculo'
        db.alter_column('interface_materialmayor', 'tipo_vehiculo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoVehiculoMaterialMayor'], null=True))

        # Adding field 'AdquisicionMaterialMayor.cuerpo_destinatario'
        db.add_column('interface_adquisicionmaterialmayor', 'cuerpo_destinatario', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.Cuerpo']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AdquisicionCompraMaterialMayor.proveedor'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'proveedor')

        # Changing field 'AdquisicionCompraMaterialMayor.orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'orden_de_compra', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.valor_final_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'valor_final_de_compra', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'AdquisicionCompraMaterialMayor.bill_of_lading'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'bill_of_lading', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.packing_list'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'packing_list', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.acta_de_recepcion'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'acta_de_recepcion', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.numero_orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'numero_orden_de_compra', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'AdquisicionCompraMaterialMayor.fecha_declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'fecha_declaracion_de_ingreso', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 9, 28, 10, 47, 12, 26597)))

        # Changing field 'AdquisicionCompraMaterialMayor.declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.numero_declaracion_de_ingreso'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'numero_declaracion_de_ingreso', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'AdquisicionCompraMaterialMayor.factura_comercial'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'factura_comercial', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.respuesta_solicitud_exencion_de_iva'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'respuesta_solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.solicitud_exencion_de_iva'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.manual_de_mantencion'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'manual_de_mantencion', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'AdquisicionCompraMaterialMayor.fecha_orden_de_compra'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'fecha_orden_de_compra', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 9, 28, 10, 47, 35, 457572)))

        # Changing field 'AdquisicionCompraMaterialMayor.agente_de_aduana'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'agente_de_aduana', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'AdquisicionCompraMaterialMayor.manual_de_usuario'
        db.alter_column('interface_adquisicioncompramaterialmayor', 'manual_de_usuario', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'MaterialMayor.pais_origen'
        db.alter_column('interface_materialmayor', 'pais_origen_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['interface.Pais']))

        # Changing field 'MaterialMayor.tipo_combustible'
        db.alter_column('interface_materialmayor', 'tipo_combustible_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.TipoCombustibleMaterialMayor']))

        # Changing field 'MaterialMayor.modelo_caja_cambio'
        db.alter_column('interface_materialmayor', 'modelo_caja_cambio_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.ModeloCajaCambioMaterialMayor']))

        # Changing field 'MaterialMayor.planos'
        db.alter_column('interface_materialmayor', 'planos', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'MaterialMayor.color'
        db.alter_column('interface_materialmayor', 'color_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.ColorMaterialMayor']))

        # Changing field 'MaterialMayor.fotografia_trasera'
        db.alter_column('interface_materialmayor', 'fotografia_trasera', self.gf('sorl.thumbnail.fields.ImageField')(default='', max_length=100))

        # Changing field 'MaterialMayor.fotografia_frontal'
        db.alter_column('interface_materialmayor', 'fotografia_frontal', self.gf('sorl.thumbnail.fields.ImageField')(default='', max_length=100))

        # Changing field 'MaterialMayor.modelo_bomba'
        db.alter_column('interface_materialmayor', 'modelo_bomba_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.ModeloBombaMaterialMayor']))

        # Changing field 'MaterialMayor.fotografia_lateral'
        db.alter_column('interface_materialmayor', 'fotografia_lateral', self.gf('sorl.thumbnail.fields.ImageField')(default='', max_length=100))

        # Changing field 'MaterialMayor.condicion'
        db.alter_column('interface_materialmayor', 'condicion_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.CondicionMaterialMayor']))

        # Changing field 'MaterialMayor.tipo_caja_cambio'
        db.alter_column('interface_materialmayor', 'tipo_caja_cambio_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.TipoCajaCambioMaterialMayor']))

        # Changing field 'MaterialMayor.ano_vehiculo'
        db.alter_column('interface_materialmayor', 'ano_vehiculo', self.gf('django.db.models.fields.IntegerField')(default=2000))

        # Changing field 'MaterialMayor.tipo_vehiculo'
        db.alter_column('interface_materialmayor', 'tipo_vehiculo_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interface.TipoVehiculoMaterialMayor']))

        # Deleting field 'AdquisicionMaterialMayor.cuerpo_destinatario'
        db.delete_column('interface_adquisicionmaterialmayor', 'cuerpo_destinatario_id')


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
            'donante': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'factura': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "['comuna', 'nombre']", 'object_name': 'Cuerpo'},
            'comuna': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Comuna']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.eventohojavidamaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'EventoHojaVidaMaterialMayor'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_mayor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MaterialMayor']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoEventoHojaVidaMaterialMayor']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'pais_origen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Pais']", 'null': 'True', 'blank': 'True'}),
            'planos': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCajaCambioMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'tipo_combustible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCombustibleMaterialMayor']", 'null': 'True', 'blank': 'True'}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoVehiculoMaterialMayor']", 'null': 'True', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.modoadquisicionmaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'ModoAdquisicionMaterialMayor'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.pais': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'interface.provincia': {
            'Meta': {'ordering': "['region', 'nombre']", 'object_name': 'Provincia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Region']"}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.reasignacioncuerpomaterialmayor': {
            'Meta': {'ordering': "['material_mayor', 'fecha']", 'object_name': 'ReasignacionCuerpoMaterialMayor', '_ormbases': ['interface.EventoHojaVidaMaterialMayor']},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']"}),
            'eventohojavidamaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.EventoHojaVidaMaterialMayor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'interface.region': {
            'Meta': {'ordering': "['numero']", 'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'webservice_id': ('django.db.models.fields.IntegerField', [], {})
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
        }
    }

    complete_apps = ['interface']
