# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents

class Region(models.Model):
    ws_id = models.IntegerField()
    numero = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.nombre

    @classmethod
    def update_all(self):
        regions_raw_data = request_webservice('/services/region/')
        raw_regions_list = regions_raw_data.childNodes
        
        for raw_region in raw_regions_list:
            region_ws_id = int(get_xml_node_contents(raw_region, 'id'))
            region_numero = int(get_xml_node_contents(raw_region, 'numero'))
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
