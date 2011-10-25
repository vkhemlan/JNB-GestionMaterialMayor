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
     
def remove_deleted_fields_from_data(data, prefix):
    total_forms = int(data['%s-TOTAL_FORMS' % prefix])
    
    return_data = {}
    insertion_index = 0
    new_initial_count = 0
    
    for i in range(total_forms):
        base_pattern = '%s-%d' % (prefix, i)
        if '%s-DELETE' % base_pattern not in data:
            for key, value in data.items():
                if base_pattern in key:
                    new_key = re.sub(r'^(%s-)\d+(-.+)$' % prefix, r'\1%d\2', key) % insertion_index
                    return_data[new_key] = value
                    if key == '%s-id' % base_pattern and value:
                        new_initial_count += 1
            insertion_index += 1
                        
    return_data['%s-TOTAL_FORMS' % prefix] = insertion_index
    return_data['%s-MAX_NUM_FORMS' % prefix] = data['%s-MAX_NUM_FORMS' % prefix]
    return_data['%s-INITIAL_FORMS' % prefix] = new_initial_count
    return return_data
