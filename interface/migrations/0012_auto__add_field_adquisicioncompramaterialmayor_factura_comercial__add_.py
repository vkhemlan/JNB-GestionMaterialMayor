# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AdquisicionCompraMaterialMayor.factura_comercial'
        db.add_column('interface_adquisicioncompramaterialmayor', 'factura_comercial', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.bill_of_lading'
        db.add_column('interface_adquisicioncompramaterialmayor', 'bill_of_lading', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.packing_list'
        db.add_column('interface_adquisicioncompramaterialmayor', 'packing_list', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.declaracion_de_ingreso'
        db.add_column('interface_adquisicioncompramaterialmayor', 'declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.numero_declaracion_de_ingreso'
        db.add_column('interface_adquisicioncompramaterialmayor', 'numero_declaracion_de_ingreso', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.fecha_declaracion_de_ingreso'
        db.add_column('interface_adquisicioncompramaterialmayor', 'fecha_declaracion_de_ingreso', self.gf('django.db.models.fields.DateField')(default=0), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.solicitud_exencion_de_iva'
        db.add_column('interface_adquisicioncompramaterialmayor', 'solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.respuesta_solicitud_exencion_de_iva'
        db.add_column('interface_adquisicioncompramaterialmayor', 'respuesta_solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.acta_de_recepcion'
        db.add_column('interface_adquisicioncompramaterialmayor', 'acta_de_recepcion', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.valor_final_de_compra'
        db.add_column('interface_adquisicioncompramaterialmayor', 'valor_final_de_compra', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.agente_de_aduana'
        db.add_column('interface_adquisicioncompramaterialmayor', 'agente_de_aduana', self.gf('django.db.models.fields.CharField')(default=0, max_length=255), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.manual_de_usuario'
        db.add_column('interface_adquisicioncompramaterialmayor', 'manual_de_usuario', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'AdquisicionCompraMaterialMayor.manual_de_mantencion'
        db.add_column('interface_adquisicioncompramaterialmayor', 'manual_de_mantencion', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AdquisicionCompraMaterialMayor.factura_comercial'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'factura_comercial')

        # Deleting field 'AdquisicionCompraMaterialMayor.bill_of_lading'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'bill_of_lading')

        # Deleting field 'AdquisicionCompraMaterialMayor.packing_list'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'packing_list')

        # Deleting field 'AdquisicionCompraMaterialMayor.declaracion_de_ingreso'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'declaracion_de_ingreso')

        # Deleting field 'AdquisicionCompraMaterialMayor.numero_declaracion_de_ingreso'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'numero_declaracion_de_ingreso')

        # Deleting field 'AdquisicionCompraMaterialMayor.fecha_declaracion_de_ingreso'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'fecha_declaracion_de_ingreso')

        # Deleting field 'AdquisicionCompraMaterialMayor.solicitud_exencion_de_iva'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'solicitud_exencion_de_iva')

        # Deleting field 'AdquisicionCompraMaterialMayor.respuesta_solicitud_exencion_de_iva'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'respuesta_solicitud_exencion_de_iva')

        # Deleting field 'AdquisicionCompraMaterialMayor.acta_de_recepcion'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'acta_de_recepcion')

        # Deleting field 'AdquisicionCompraMaterialMayor.valor_final_de_compra'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'valor_final_de_compra')

        # Deleting field 'AdquisicionCompraMaterialMayor.agente_de_aduana'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'agente_de_aduana')

        # Deleting field 'AdquisicionCompraMaterialMayor.manual_de_usuario'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'manual_de_usuario')

        # Deleting field 'AdquisicionCompraMaterialMayor.manual_de_mantencion'
        db.delete_column('interface_adquisicioncompramaterialmayor', 'manual_de_mantencion')


    models = {
        'interface.adquisicioncompramaterialmayor': {
            'Meta': {'object_name': 'AdquisicionCompraMaterialMayor', '_ormbases': ['interface.MaterialMayor']},
            'acta_de_recepcion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'agente_de_aduana': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bill_of_lading': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'declaracion_de_ingreso': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'factura_comercial': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'fecha_declaracion_de_ingreso': ('django.db.models.fields.DateField', [], {}),
            'fecha_orden_de_compra': ('django.db.models.fields.DateField', [], {}),
            'manual_de_mantencion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'manual_de_usuario': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'materialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.MaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'numero_declaracion_de_ingreso': ('django.db.models.fields.IntegerField', [], {}),
            'numero_orden_de_compra': ('django.db.models.fields.IntegerField', [], {}),
            'orden_de_compra': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'packing_list': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'respuesta_solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'valor_final_de_compra': ('django.db.models.fields.IntegerField', [], {})
        },
        'interface.colormaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'ColorMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'interface.condicionmaterialmayor': {
            'Meta': {'ordering': "['name']", 'object_name': 'CondicionMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'ano_vehiculo': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ColorMaterialMayor']"}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.CondicionMaterialMayor']"}),
            'fotografia_frontal': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'fotografia_lateral': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'fotografia_trasera': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo_bomba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloBombaMaterialMayor']"}),
            'modelo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCajaCambioMaterialMayor']"}),
            'modelo_carrosado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCarrosadoMaterialMayor']"}),
            'modelo_chasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloChasisMaterialMayor']"}),
            'modo_adquisicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModoAdquisicionMaterialMayor']"}),
            'numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pais_origen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Pais']"}),
            'placa_patente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCajaCambioMaterialMayor']"}),
            'tipo_combustible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoCombustibleMaterialMayor']"}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoVehiculoMaterialMayor']"})
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
        'interface.modelocarrosadomaterialmayor': {
            'Meta': {'ordering': "['marca', 'name']", 'object_name': 'ModeloCarrosadoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaCarrosadoMaterialMayor']"}),
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
            'Meta': {'ordering': "['name']", 'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'interface.tipovehiculomaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'TipoVehiculoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['interface']
