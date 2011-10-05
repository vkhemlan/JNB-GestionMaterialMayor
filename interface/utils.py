import logging
from django.conf import settings
from xml.dom.minidom import parseString
import urllib2
import re

def log(message):
    logger = logging.getLogger(settings.PROJECT_MODULE)
    logger.info(message)

def update_data_from_webservice():
    from models import Region, Provincia, Comuna, Cuerpo, Compania
    for layer in [Region, Provincia, Comuna, Cuerpo, Compania]:
        layer.update_from_webservice()

def request_webservice(service_location, data=None):
    request = urllib2.Request(
        url='%s%s' % (settings.JNB_WEBSERVICES_URL, service_location,), 
        data=data, 
        headers={
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Accept':'application/xml'})
    f = urllib2.urlopen(request)
    xml_data = parseString(f.read())
    return xml_data.childNodes[0]
    
def get_xml_node_contents(xml, node_name):
    '''
    Method that, given an XML object and one of the root's child name, 
    returns its contents
    '''
    return xml.getElementsByTagName(node_name)[0].childNodes[0].nodeValue

def get_xml_node_attribute(xml, node_name, attribute_name):
    return xml.getElementsByTagName(node_name)[0].attributes.get(attribute_name).value
    
def get_xml_node_children(xml, node_name):
    return xml.getElementsByTagName(node_name)
    
def convert_camelcase_to_lowercase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
def intersect(a, b):
     return bool(set(a) & set(b))
    
def uploaded_document_rename(container_attribute, field_name, instance, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'documentos/%d_%s-%s.%s' % (instance.id, container_attribute, field_name, extension)
    
def generate_uploaded_hoja_de_vida_file_name(field_name, evento, filename):
    left_path, extension = filename.rsplit('.',1)
    
    return 'documentos/material_mayor/%d/evento_hoja_vida/%d-%s.%s' % (evento.material_mayor.id, evento.id, field_name, extension)
