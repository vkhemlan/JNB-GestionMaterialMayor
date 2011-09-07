# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MaterialMayor'
        db.create_table('interface_materialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoVehiculoMaterialMayor'])),
            ('marca_chasis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaChasisMaterialMayor'])),
            ('modelo_chasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero_chasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero_motor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('placa_patente', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ano_vehiculo', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ColorMaterialMayor'])),
        ))
        db.send_create_signal('interface', ['MaterialMayor'])


    def backwards(self, orm):
        
        # Deleting model 'MaterialMayor'
        db.delete_table('interface_materialmayor')


    models = {
        'interface.colormaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'ColorMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'interface.marcachasismaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'MarcaChasisMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'interface.materialmayor': {
            'Meta': {'object_name': 'MaterialMayor'},
            'ano_vehiculo': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ColorMaterialMayor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca_chasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.MarcaChasisMaterialMayor']"}),
            'modelo_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'placa_patente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo_vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.TipoVehiculoMaterialMayor']"})
        },
        'interface.tipovehiculomaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'TipoVehiculoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['interface']
