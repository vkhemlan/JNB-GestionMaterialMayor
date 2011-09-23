# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TipoVehiculoMaterialMayor'
        db.create_table('interface_tipovehiculomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
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
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('interface', ['ColorMaterialMayor'])

        # Adding model 'MaterialMayor'
        db.create_table('interface_materialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoVehiculoMaterialMayor'])),
            ('modelo_chasis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloChasisMaterialMayor'])),
            ('numero_chasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero_motor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ano_vehiculo', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ColorMaterialMayor'])),
            ('modelo_carrosado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloCarrosadoMaterialMayor'])),
            ('condicion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.CondicionMaterialMayor'])),
            ('modelo_caja_cambio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloCajaCambioMaterialMayor'])),
            ('tipo_caja_cambio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCajaCambioMaterialMayor'])),
            ('tipo_combustible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.TipoCombustibleMaterialMayor'])),
            ('modelo_bomba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.ModeloBombaMaterialMayor'])),
            ('pais_origen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Pais'])),
            ('fotografia_frontal', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('fotografia_lateral', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('fotografia_trasera', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('adquisicion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True)),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Cuerpo'], null=True, blank=True)),
            ('compania', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.Compania'], null=True, blank=True)),
        ))
        db.send_create_signal('interface', ['MaterialMayor'])

        # Adding model 'ModeloChasisMaterialMayor'
        db.create_table('interface_modelochasismaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaChasisMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModeloChasisMaterialMayor'])

        # Adding model 'MarcaCarrosadoMaterialMayor'
        db.create_table('interface_marcacarrosadomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['MarcaCarrosadoMaterialMayor'])

        # Adding model 'ModeloCarrosadoMaterialMayor'
        db.create_table('interface_modelocarrosadomaterialmayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interface.MarcaCarrosadoMaterialMayor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interface', ['ModeloCarrosadoMaterialMayor'])

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
        ))
        db.send_create_signal('interface', ['AdquisicionMaterialMayor'])

        # Adding model 'AdquisicionCompraMaterialMayor'
        db.create_table('interface_adquisicioncompramaterialmayor', (
            ('adquisicionmaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True, primary_key=True)),
            ('orden_de_compra', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('numero_orden_de_compra', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_orden_de_compra', self.gf('django.db.models.fields.DateField')()),
            ('factura_comercial', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('bill_of_lading', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('packing_list', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('declaracion_de_ingreso', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('numero_declaracion_de_ingreso', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_declaracion_de_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('respuesta_solicitud_exencion_de_iva', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('acta_de_recepcion', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('valor_final_de_compra', self.gf('django.db.models.fields.IntegerField')()),
            ('agente_de_aduana', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('manual_de_usuario', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('manual_de_mantencion', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('interface', ['AdquisicionCompraMaterialMayor'])

        # Adding model 'AdquisicionDonacionMaterialMayor'
        db.create_table('interface_adquisiciondonacionmaterialmayor', (
            ('adquisicionmaterialmayor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['interface.AdquisicionMaterialMayor'], unique=True, primary_key=True)),
            ('donante', self.gf('django.db.models.fields.CharField')(max_length=255)),
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


    def backwards(self, orm):
        
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

        # Deleting model 'ModeloCarrosadoMaterialMayor'
        db.delete_table('interface_modelocarrosadomaterialmayor')

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


    models = {
        'interface.adquisicioncompramaterialmayor': {
            'Meta': {'object_name': 'AdquisicionCompraMaterialMayor', '_ormbases': ['interface.AdquisicionMaterialMayor']},
            'acta_de_recepcion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'adquisicionmaterialmayor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['interface.AdquisicionMaterialMayor']", 'unique': 'True', 'primary_key': 'True'}),
            'agente_de_aduana': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bill_of_lading': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'declaracion_de_ingreso': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'factura_comercial': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'fecha_declaracion_de_ingreso': ('django.db.models.fields.DateField', [], {}),
            'fecha_orden_de_compra': ('django.db.models.fields.DateField', [], {}),
            'manual_de_mantencion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'manual_de_usuario': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'numero_declaracion_de_ingreso': ('django.db.models.fields.IntegerField', [], {}),
            'numero_orden_de_compra': ('django.db.models.fields.IntegerField', [], {}),
            'orden_de_compra': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'packing_list': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'respuesta_solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'solicitud_exencion_de_iva': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'valor_final_de_compra': ('django.db.models.fields.IntegerField', [], {})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModoAdquisicionMaterialMayor']"})
        },
        'interface.colormaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'ColorMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'ano_vehiculo': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ColorMaterialMayor']"}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Compania']", 'null': 'True', 'blank': 'True'}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.CondicionMaterialMayor']"}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Cuerpo']", 'null': 'True', 'blank': 'True'}),
            'fotografia_frontal': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'fotografia_lateral': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'fotografia_trasera': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo_bomba': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloBombaMaterialMayor']"}),
            'modelo_caja_cambio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCajaCambioMaterialMayor']"}),
            'modelo_carrosado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloCarrosadoMaterialMayor']"}),
            'modelo_chasis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.ModeloChasisMaterialMayor']"}),
            'numero_chasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_motor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pais_origen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['interface.Pais']"}),
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
        'interface.tipovehiculomaterialmayor': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'TipoVehiculoMaterialMayor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['interface']
