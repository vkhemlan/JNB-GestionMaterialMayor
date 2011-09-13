# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CondicionMaterialMayor'
        db.create_table('interface_condicionmaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['CondicionMaterialMayor'])

        # Adding model 'ModeloCarrosadoMaterialMayor'
        db.create_table('interface_modelocarrosadomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaCarrosadoMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModeloCarrosadoMaterialMayor'])

        # Adding model 'MarcaCarrosadoMaterialMayor'
        db.create_table('interface_marcacarrosadomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaCarrosadoMaterialMayor'])

        # Adding field 'MaterialMayor.modelo_carrosado'
        db.add_column('interface_materialmayor', 'modelo_carrosado', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['interface.ModeloCarrosadoMaterialMayor']), keep_default=False)

        # Adding field 'MaterialMayor.condicion'
        db.add_column('interface_materialmayor', 'condicion', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['interface.CondicionMaterialMayor']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'CondicionMaterialMayor'
        db.delete_table('interface_condicionmaterialmayor')

        # Deleting model 'ModeloCarrosadoMaterialMayor'
        db.delete_table('interface_modelocarrosadomaterialmayor')

        # Deleting model 'MarcaCarrosadoMaterialMayor'
        db.delete_table('interface_marcacarrosadomaterialmayor')

        # Deleting field 'MaterialMayor.modelo_carrosado'
        db.delete_column('interface_materialmayor', 'modelo_carrosado_id')

        # Deleting field 'MaterialMayor.condicion'
        db.delete_column('interface_materialmayor', 'condicion_id')


    models = {
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo_carrosado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCarrosadoMaterialMayor']"}),
            'modelo_chasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloChasisMaterialMayor']"}),
            'numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'placa_patente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoVehiculoMaterialMayor']"})
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
        'interface.tipovehiculomaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'TipoVehiculoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['interface']
