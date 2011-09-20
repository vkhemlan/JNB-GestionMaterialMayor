# coding: utf-8

from django.db import models
from interface.utils import request_webservice, get_xml_node_contents, get_xml_node_attribute

class Compania(models.Model):
    webservice_id = models.IntegerField()
    numero = models.IntegerField()
    cuerpo = models.ForeignKey('Cuerpo')
        
    def __unicode__(self):
        return self.string_number()
        
    def string_number(self):
        '''
        Converts the company number to corresponding string (e.g. 1 => "Primera")
        '''
        conversion_table = ['',
            u'Primera',
            u'Segunda',
            u'Tercera',
            u'Cuarta',
            u'Quinta',
            u'Sexta',
            u'Séptima',
            u'Octava',
            u'Novena',
            u'Décima',
            u'Undécima',
            u'Duodécima',
            u'Décimotercera',
            u'Décimocuarta',
            u'Décimoquinta',
            u'Décimosexta',
            u'Decimoséptima',
            u'Decimooctava',
            u'Decimonovena',
            u'Vigésima',
            u'Vigésimoprimera',
            u'Vigésimosegunda',
        ]
        try:
            return conversion_table[self.numero] + u' Compañía'
        except IndexError:
            return ''

    @classmethod
    def update_from_webservice(self):
        from . import Cuerpo

        companias_raw_data = request_webservice('/services/compania/')
        raw_companias_list = companias_raw_data.childNodes
        
        for raw_compania in raw_companias_list:
            compania_webservice_id = int(get_xml_node_contents(raw_compania, 'id'))
            compania_cuerpo_id = int(get_xml_node_attribute(raw_compania, 'cuerpo', 'id'))
            compania_numero = int(get_xml_node_contents(raw_compania, 'numero'))
            
            try:
                compania = Compania.objects.get(webservice_id=compania_webservice_id)
            except Compania.DoesNotExist:
                compania = Compania()
                compania.webservice_id = compania_webservice_id

            compania.cuerpo = Cuerpo.objects.get(webservice_id=compania_cuerpo_id)
            compania.numero = compania_numero

            compania.save()

    class Meta:
        ordering = ['cuerpo', 'numero']
        app_label = 'interface'
        verbose_name = u'Compañía'
        verbose_name_plural = u'Compañías'
