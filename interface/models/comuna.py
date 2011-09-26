# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents, get_xml_node_attribute, log

class Comuna(models.Model):
    webservice_id = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    provincia = models.ForeignKey('Provincia')
    
    def __unicode__(self):
        return self.nombre

    @classmethod
    def update_from_webservice(self):
        log('Actualizando comunas desde Webservice')
        from . import Provincia

        comunas_raw_data = request_webservice('/services/comuna/')
        raw_comunas_list = comunas_raw_data.childNodes
        
        for raw_comuna in raw_comunas_list:
            comuna_webservice_id = int(get_xml_node_contents(raw_comuna, 'id'))
            comuna_provincia_id = int(get_xml_node_attribute(raw_comuna, 'provincia', 'id'))
            comuna_nombre = get_xml_node_contents(raw_comuna, 'nombre')
            log('%d %d %s' % (comuna_webservice_id, comuna_provincia_id, comuna_nombre))
            
            try:
                comuna = Comuna.objects.get(webservice_id=comuna_webservice_id)
            except Comuna.DoesNotExist:
                comuna = Comuna()
                comuna.webservice_id = comuna_webservice_id

            comuna.provincia = Provincia.objects.get(webservice_id=comuna_provincia_id)
            comuna.nombre = comuna_nombre

            comuna.save()
            log('Comuna guardada')

    class Meta:
        ordering = ['provincia', 'nombre']
        app_label = 'interface'
        verbose_name = u'Comuna'
        verbose_name_plural = u'Comunas'
