# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents

class Provincia(models.Model):
    ws_id = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    region = models.ForeignKey('Region')
    
    def __unicode__(self):
        return self.nombre

    @classmethod
    def update_all(self):
        provinces_raw_data = request_webservice('/services/provincia/')
        raw_provinces_list = provinces_raw_data.childNodes
        
        for raw_province in raw_provinces_list:
            # TODO PENDING
            province_ws_id = int(get_xml_node_contents(raw_province, 'id'))
            province_region_id = int(get_xml_node_contents(raw_region, 'numero'))
            region_nombre = get_xml_node_contents(raw_region, 'nombre')
            
            region, created = Region.objects.get_or_create(ws_id=region_ws_id)
            region.numero = region_numero
            region.nombre = region_nombre
            region.save()

    class Meta:
        ordering = ['numero']
        app_label = 'interface'
        verbose_name = u'Región'
        verbose_name_plural = u'Regiones'
