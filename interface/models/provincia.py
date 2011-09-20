# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents, get_xml_node_attribute

class Provincia(models.Model):
    webservice_id = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    region = models.ForeignKey('Region')
    
    def __unicode__(self):
        return self.nombre

    @classmethod
    def update_from_webservice(self):
        from . import Region

        provincias_raw_data = request_webservice('/services/provincia/')
        raw_provincias_list = provincias_raw_data.childNodes
        
        for raw_provincia in raw_provincias_list:
            provincia_webservice_id = int(get_xml_node_contents(raw_provincia, 'id'))
            provincia_region_id = int(get_xml_node_attribute(raw_provincia, 'region', 'id'))
            provincia_nombre = get_xml_node_contents(raw_provincia, 'nombre')
            
            try:
                provincia = Provincia.objects.get(webservice_id=provincia_webservice_id)
            except Provincia.DoesNotExist:
                provincia = Provincia()
                provincia.webservice_id = provincia_webservice_id

            provincia.region = Region.objects.get(webservice_id=provincia_region_id)
            provincia.nombre = provincia_nombre

            provincia.save()

    class Meta:
        ordering = ['region', 'nombre']
        app_label = 'interface'
        verbose_name = u'Provincia'
        verbose_name_plural = u'Provincias'
