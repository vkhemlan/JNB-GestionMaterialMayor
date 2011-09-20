# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents, get_xml_node_attribute

class Cuerpo(models.Model):
    webservice_id = models.IntegerField()
    nombre = models.CharField(max_length = 255)
    comuna = models.ForeignKey('Comuna')
    
    def __unicode__(self):
        return 'Cuerpo de %s ' % (self.nombre,)

    @classmethod
    def update_from_webservice(self):
        from . import Comuna

        cuerpos_raw_data = request_webservice('/services/cuerpo/')
        raw_cuerpos_list = cuerpos_raw_data.childNodes
        
        for raw_cuerpo in raw_cuerpos_list:
            cuerpo_webservice_id = int(get_xml_node_contents(raw_cuerpo, 'id'))
            cuerpo_comuna_id = int(get_xml_node_attribute(raw_cuerpo, 'comuna', 'id'))
            cuerpo_nombre = get_xml_node_contents(raw_cuerpo, 'nombre')
            
            try:
                cuerpo = Cuerpo.objects.get(webservice_id=cuerpo_webservice_id)
            except Cuerpo.DoesNotExist:
                cuerpo = Cuerpo()
                cuerpo.webservice_id = cuerpo_webservice_id

            cuerpo.comuna = Comuna.objects.get(webservice_id=cuerpo_comuna_id)
            cuerpo.nombre = cuerpo_nombre

            cuerpo.save()

    class Meta:
        ordering = ['comuna', 'nombre']
        app_label = 'interface'
        verbose_name = u'Cuerpo'
        verbose_name_plural = u'Cuerpos'
